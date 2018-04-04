# View的工作原理

## ViewRoot & DecorView

ViewRoot -> ViewRootImpl, 它是连接WindowManager和DecorView的纽带，View的三大流程均是通过ViewRootlmpl完成。

performMeasure -> measure -> onMeasure
performLayout -> layout  -> onLayout
performDraw   -> draw -> onDraw&dispatchDraw

### MeasureSpec

SpecMode/SpecSize

SpecMode有三类：
* unspecified
  父容器不对View有任何限制

* exactly    
  父容器已经检测出View所需要的精确大小，这个时候View的大小就是SpecSize所指定的值。它对应于LayoutParams中的match_parent和具体的数值这两种模式。

* at_most
  父容器指定了一个可用大小即SpecSize，View的大小不能大于这个值，具体是什么值要看不同View的具体实现。它对应于LayoutParams中的wrap_content.

### MeasureSpec 和 LayoutParams的对应关系

LayoutParams需要和父容器一起才能决定View的MeasureSpec，从而进一步决定View的宽/高。对于DecorView，其MeasureSpec由窗口的尺寸和其自身的LayoutParams来共同决定；对于普通View，其MeasureSpec由父容器的MeasureSpec和自身的LayoutParams来共同决定，MeasureSpec一旦确定后，onMeasure中就可以确定View的测量宽/高。

View的measure过程由ViewGroup传递而来，看ViewGroup的measureChildWithMargins方法：

```java
    protected void measureChildWithMargins(View child,
            int parentWidthMeasureSpec, int widthUsed,
            int parentHeightMeasureSpec, int heightUsed) {
        final MarginLayoutParams lp = (MarginLayoutParams) child.getLayoutParams();

        final int childWidthMeasureSpec = getChildMeasureSpec(parentWidthMeasureSpec,
                mPaddingLeft + mPaddingRight + lp.leftMargin + lp.rightMargin
                        + widthUsed, lp.width);
        final int childHeightMeasureSpec = getChildMeasureSpec(parentHeightMeasureSpec,
                mPaddingTop + mPaddingBottom + lp.topMargin + lp.bottomMargin
                        + heightUsed, lp.height);

        child.measure(childWidthMeasureSpec, childHeightMeasureSpec);
    }
```
