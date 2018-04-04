# UI更新与主线程

## 程序中自定义Thread和UI线程的区别是什么？

UI线程是从ActivityThread运行的，在该类中的main()方法中，已经使用Looper.prepareMainLooper()为该线程添加了Looper对象，即已经为该线程创建了消息队列(MessageQueue)，而普通的自定义Thread是一个裸线程，因此，不能直接在Thread中定义Hander对象。


## 子线程为什么不能更新UI

因为UI访问是没有加锁的，在多个线程中访问UI是不安全的，如果有多个子线程都去更新UI，会导致界面不断改变而混乱不堪。所以最好的解决办法就是只有一个线程有更新UI的权限。

## 子线程也可以更新UI
SurfaceView可以在主线程之外的线程中向屏幕绘图。这样可以避免画图任务繁重的时候造成主线程阻塞，从而提高了程序的反应速度。

## 子线程可以更新除SurfaceView以外的UI
```java
public class MainActivity extends Activity {

    private TextView mTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mTextView=(TextView)findViewById(R.id.textView);

        new Thread(new Runnable() {
            @Override
            public void run() {
                mTextView.setText("onCreate-new-thread");
            }
        }).start();
    }
}
```
一个应用程序中有一个主线程和若干个子线程，而线程的检查工作是由ViewRoot完成的。而ViewRoot的创建是在onResume（）之后才完成的，也就是说在onResume（）之前，系统本身是无法区分当前线程到底是主线程还是子线程，而上面的代码中UI的更新操作在onCreate（）中完成，先于onResume（），所以上述的子线程才能设置UI。
