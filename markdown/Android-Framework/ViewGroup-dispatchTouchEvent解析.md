#  dispatchTouchEvent (2.3.6)
```java

 boolean disallowIntercept = (mGroupFlags & FLAG_DISALLOW_INTERCEPT) != 0;

 if (action == MotionEvent.ACTION_DOWN) {
      if (mMotionTarget != null) { //Down 事件 清空mMotionTarget赋值
        mMotionTarget = null;
      }
      //不允许拦截事件 || 允许而不拦截事件；则寻找响应事件的子View
     if (disallowIntercept || !onInterceptTouchEvent(ev)) {
       for (int i = count - 1; i >= 0; i--) {
            final View child = children[i];
            child.getHitRect(frame);
            if (frame.contains(scrolledXInt, scrolledYInt)) {
              if (child.dispatchTouchEvent(ev))  {
                // Event handled, we have a target now.
                mMotionTarget = child;
                return true;
               }
            }
          }
     } // end ACTION_DOWN


     final View target = mMotionTarget;
     //子View不处理触摸事件
     if (target == null) {
       return super.dispatchTouchEvent(ev); //最终调用View类 onTouchEvent 方法
     }

     //拦截触摸事件
     if (!disallowIntercept && onInterceptTouchEvent(ev)) {
       ev.setAction(MotionEvent.ACTION_CANCEL); //给响应的子View一个CANCEL事件
       if (!target.dispatchTouchEvent(ev)) {

       }
       mMotionTarget = null;
       return true;
     }
     //事件分发给子View处理
     return target.dispatchTouchEvent(ev);
  }
  ```
