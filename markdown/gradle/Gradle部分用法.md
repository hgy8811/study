## gradle
文件依赖
```java
dependencies {
       compile files('libs/domoarigato.jar')
}
```
如果你这么做，那会很愚蠢，因为当你有很多这样的jar包时，你可以改写为：
```java
dependencies {
       compile fileTree('libs')
 }
```

默认情况下，新建的Android项目会有一个lib文件夹，并且会在依赖中这么定义（即添加所有在libs文件夹中的jar）：

```java
dependencies {
       compile fileTree(dir: 'libs', include: ['*.jar'])
}
```

###  gradle tasks查看任务信息
./gradlew project-path:tasks (exp: ./gradlew :app:tasks)

### gradle task-name执行任务
1. gradle clean是执行清理任务，和make clean类似。
2. gradle properites用来查看所有属性信息。
