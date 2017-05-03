# Android性能优化典范(一)
主要从 Android 的渲染机制、内存与 GC、电量优化三个方面展开，介绍了 Android 中性能问题的底层工作原理，以及如何通过工具来找出性能问题及提升性能的建议。

1. 渲染性能 [Render Performance]
 16ms内渲染完成 -> 60fps
 丢帧：layout太过复杂，无法在16ms内完成渲染，有可能是因为你的UI上有层叠太多的绘制单元，还有可能是因为动画执行的次数过多。这些都会导致CPU或者GPU负载过重。

 2. 理解过度绘制 [Understanding Overdraw]
 Overdraw(过度绘制)描述的是屏幕上的某个像素在同一帧的时间内被绘制了多次，浪费大量的CPU以及GPU资源。
 Overdraw有时候是因为你的UI布局存在大量重叠的部分，还有的时候是因为非必须的重叠背景。

 3. Understanding VSYNC

 4. Tool:Profile GPU Rendering

 5. Why 60fps?
需要用到60fps来顺畅表现绚丽的画面内容，当然超过60fps是没有必要的。
开发app的性能目标就是保持60fps，这意味着每一帧你只有16ms=1000/60的时间来处理所有的任务。

6. Android, UI and the GPU

CPU负责把UI组件计算成Polygons，Texture纹理，然后交给GPU进行栅格化渲染。
为了能够使得App流畅，我们需要在每一帧16ms以内处理完所有的CPU与GPU计算，绘制，渲染等等操作。

7. Invalidations, Layouts, and Performance
Android需要把XML布局文件转换成GPU能够识别并绘制的对象。这个操作是在DisplayList的帮助下完成的。DisplayList持有所有将要交给GPU绘制到屏幕上的数据信息。
任何时候View中的绘制内容发生变化时，都会重新执行创建DisplayList，渲染DisplayList，更新到屏幕上等一系列操作。这个流程的表现性能取决于你的View的复杂程度，View的状态变化以及渲染管道的执行性能。

使得布局尽量扁平化，移除非必需的UI组件，这些操作能够减少Measure，Layout的计算时间。

8. Overdraw, Cliprect, QuickReject
通过canvas.clipRect()来帮助系统识别那些可见的区域。这个方法可以指定一块矩形区域，只有在这个区域内才会被绘制，其他的区域会被忽视。
同时clipRect方法还可以帮助节约CPU与GPU资源，在clipRect区域之外的绘制指令都不会被执行，那些部分内容在矩形区域内的组件，仍然会得到绘制。
还可以使用canvas.quickreject()来判断是否没和某个矩形相交，从而跳过那些非矩形区域内的绘制操作。做了那些优化之后，我们可以通过上面介绍的Show GPU Overdraw来查看效果。

9. Memory Churn and performance
虽然Android有自动管理内存的机制，但是对内存的不恰当使用仍然容易引起严重的性能问题。在同一帧里面创建过多的对象是件需要特别引起注意的事情。大量不停的GC操作则会显著占用帧间隔时间.

导致GC频繁执行有两个原因：Memory Churn内存抖动;瞬间产生大量的对象，引起GC。
通过对象池来解决频繁创建与销毁的问题。

10. Garbage Collection in Android

内存分代管理，GC导致性能问题


11. Performance Cost of Memory Leaks
内存泄漏

12. Memory Performance
如果我们对内存的使用不恰当，导致GC频繁执行，这样就会引起不小的性能问题。
Android Studio提供的内存的性能问题查看工具:
Memory Monitor：查看整个app所占用的内存，以及发生GC的时刻，短时间内发生大量的GC操作是一个危险的信号。
Allocation Tracker：使用此工具来追踪内存的分配，前面有提到过。
Heap Tool：查看当前内存快照，便于对比分析哪些对象有可能是泄漏了的，请参考前面的Case。

13. Tool - Memory Monitor

14. Battery Performance
减少电量的消耗：
尽量减少唤醒屏幕的次数与持续的时间，使用WakeLock来处理唤醒的问题；
非必须立刻执行的操作，电量充足再做；
网络数据打包批处理；
15. Understanding Battery Drain on Android

使用WakeLock或者JobScheduler唤醒设备处理定时的任务之后，一定要及时让设备回到初始状态。

16. Battery Drain and WakeLocks
使用非精准定时器，降低唤醒频率；
