# View的事件体系

Touch传递处理流程

```java
public boolean dispatchTouchEvent(MotionEvent ev){
  boolean consume = false;
  if(onInterceptTouchEvent(ev)){
    consume = onTouchEvent(ev);
  }else{
    consume = child.dispatchTouchEvent(ev);
  }

  return consume;
}
```
