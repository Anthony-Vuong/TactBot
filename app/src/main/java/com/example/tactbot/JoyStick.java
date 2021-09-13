package com.example.tactbot;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.PorterDuff;
import android.util.AttributeSet;
import android.util.Log;
import android.view.MotionEvent;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;

import androidx.annotation.NonNull;

public class JoyStick extends SurfaceView implements SurfaceHolder.Callback, View.OnTouchListener {

    private float centerX;
    private float centerY;
    private float baseRadius;
    private float hatRadius;
    private JoystickListener joystickCallback;


    private void setupDimensions()
    {
        centerX = getWidth() / 2;
        centerY = getHeight() / 2;
        baseRadius = Math.min(getWidth(), getHeight()) / 3;
        hatRadius = Math.min(getWidth(), getHeight()) / 5;
    }

    public JoyStick(Context context)
    {
        super(context);
        getHolder().addCallback(this);
        setOnTouchListener(this);
        if(context instanceof JoystickListener)
            joystickCallback = (JoystickListener) context;


    }

    public JoyStick(Context context, AttributeSet attributes, int style)
    {
        super(context, attributes, style);
        getHolder().addCallback(this);
        setOnTouchListener(this);
        if(context instanceof JoystickListener)
            joystickCallback = (JoystickListener) context;


    }

    public JoyStick(Context context, AttributeSet attributes)
    {
        super(context, attributes);
        getHolder().addCallback(this);
        setOnTouchListener(this);
        if(context instanceof JoystickListener)
            joystickCallback = (JoystickListener) context;

    }

    private void drawJoystick(float newX, float newY){
        if(getHolder().getSurface().isValid()) {
            Canvas myCanvas = this.getHolder().lockCanvas();
            Paint colors = new Paint();
            myCanvas.drawColor(Color.TRANSPARENT, PorterDuff.Mode.CLEAR);
            colors.setARGB(255, 50, 50, 50);
            myCanvas.drawCircle(centerX, centerY, baseRadius, colors);
            colors.setARGB(255, 0, 0, 255);
            myCanvas.drawCircle(newX, newY, hatRadius, colors);
            getHolder().unlockCanvasAndPost(myCanvas);
        }
    }


    @Override
    public void surfaceCreated(@NonNull SurfaceHolder holder) {

        setupDimensions();
        drawJoystick(centerX, centerY);
    }

    @Override
    public void surfaceChanged(@NonNull SurfaceHolder holder, int format, int width, int height) {

    }

    @Override
    public void surfaceDestroyed(@NonNull SurfaceHolder holder) {

    }

    @Override
    public boolean onTouch(View v, MotionEvent event) {
        if(v.equals(this)){

            if(event.getAction() != event.ACTION_UP){
                float displacement = (float)Math.sqrt(Math.pow(event.getX() - centerX, 2) + Math.pow(event.getY() - centerY, 2));

                if(displacement < baseRadius){
                    drawJoystick(event.getX(), event.getY());
                    joystickCallback.onJoystickMoved((event.getX() - centerX)/baseRadius, (event.getY() - centerY)/baseRadius, getId());


                }
                else{
                    float ratio = baseRadius / displacement;
                    float constrainedX = centerX + (event.getX() - centerX) * ratio;
                    float constrainedY = centerY + (event.getY() - centerY) * ratio;

                    drawJoystick(constrainedX, constrainedY);
                    joystickCallback.onJoystickMoved((constrainedX-centerX)/baseRadius, (constrainedY-centerY)/baseRadius, getId());

                }
            }
            else{
                drawJoystick(centerX, centerY);
                joystickCallback.onJoystickMoved(0,0,getId());
            }
        }
        return true;
    }

    public interface JoystickListener
    {
        void onJoystickMoved(float xPercent, float yPercent, int id);
    }
}
