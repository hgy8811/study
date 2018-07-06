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

## 点击事件传递规则
1. 同一个事件序列是指从手指触摸屏幕开始，到手指离开屏幕结束，这个过程中产生的一系列事件：down move... up

2. 一般一个事件序列只能被一个View拦截并消耗。因为一旦一个元素拦截了某事件，那么同一事件序列内的所有事件都会直接交给它处理，因此不能
   分别由两个View同时处理，但通过特殊手段可以做到，比如一个View调用别的View的onTouchEvent方法

3. 某个View一旦拦截，那么这一事件序列都只能由它来处理，并且他的onInterceptTouchEvent不会再被调用。

4. 某个View一旦开始处理事件，如果它不消耗ACTION_DOWN事件(onTouchEvent返回false)，那么同一事件序列中的其他事件都不会再交给它来
   处理，并且事件将重新交给它的父元素去处理，即父元素的onTouchEvent会被调用。
5. 如果View不消耗除ACTION_DOWN以外的其他事件，那么这个点击事件会消失，此时父元素的onTouchEvent并不会被调用，并且当前View可以收到
   后续的事件，最终这些消失的点击事件会传递给Activity处理。

6. ViewGroup默认不拦截任何事件。

7. View没有onInterceptTouchEvent方法，一旦有点击事件传递给它，那么它的onTouchEvent方法就会被调用

8. View的onTouchEvent默认都会消耗事件(返回true)，除非它是不可点击的(clickable和longClickable同时为false)。View的longClickable默认为false,clickable属性要分情况，比如Button默认为true，而TextView默认为false

9. View的enable属性不影响onTouchEvent的默认返回值，只跟clickable和longClickable属性有关。

10. onClick会发生的前提是当前View是可点击的，并且收到down和up的事件

11. 事件传递过程是由外向内的，即事件总是先传递给父元素，然后再由父元素分发给子View，通过requestDisallowInterceptTouchEvent
    方法可以在子元素干预父元素的时间分发过程，但是ACTION_DOWN事件除外。


## View的滑动冲突

### 常见滑动冲突场景
1. 外部滑动方向和内部滑动方向不一致
2. 外部滑动方向和内部滑动方向一致
3. 上面两种情况的嵌套

### 滑动冲突解决方式
1. 外部拦截法 [重写父容器的onInterceptTouchEvent方法]
2. 内部拦截法 [重写子元素的dispatchTouchEvent,配合requestDisallowTouchEvent，父元素也要默认拦截处理ACTION_DOWN以外的其他事件]
