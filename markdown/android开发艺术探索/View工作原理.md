# View工作原理

measure、layout、draw

## draw过程

1. 绘制背景      background.draw(canvas)
2. 绘制自己      onDraw
3. 绘制children  dispatchDraw
4. 绘制装饰       onDrawScrollBars

## 自定义View的分类

1. 继承View重写onDraw方法
   需要自己支持wrap_content,并且padding也需自己处理。
2. 继承ViewGroup派生特殊的Layout
   需要核实处理ViewGroup的测量、布局这两个过程，并同时处理子元素的测量和布局过程。
3. 继承特定的View (如TextView)
   比较容易实现
4. 继承特定的ViewGroup（如LinearLayout）
   类比2，不需要处理测量和布局过程，更简单
