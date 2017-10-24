# Swiper滑动插件
- [Swiper官网](http://www.swiper.com.cn/),幻灯效果
- 在PC端实现过一次，主要使用的是其demo21---自动滑动
- 简单的引入js和css,编辑swiper-slide div内的内容
```
<html>
<head>
    <style>
        .swiper-container {
            width: 100%;
            height: 100%;
        }
        .swiper-slide {
            text-align: center; 
            font-size: 18px;
            background: #fff;
            /* Center slide text vertically */
            display: -webkit-box;
            display: -ms-flexbox;
            display: -webkit-flex;
            display: flex;
            -webkit-box-pack: center;
            -ms-flex-pack: center;
            -webkit-justify-content: center;
            justify-content: center;
            -webkit-box-align: center;
            -ms-flex-align: center;
            -webkit-align-items: center;
            align-items: center;
        } 
    </style>
    <script src="~/Content/Portal/swiper.min.js"></script>
    <link rel="stylesheet" href="~/Content/Portal/swiper.min.css" type="text/css" /> 
</head>
<body>
    <div class="swiper-container">
        <div class="swiper-wrapper">
            <div class="swiper-slide">
                <img src="~/Content/Portal/37e7e6855aa14740970e53b2c1004474.png" width="510"/>
            </div>
            <div class="swiper-slide">
                <img src="~/Content/Portal/7bd01015fd984881a6b8d55c141208fb.png" width="510"/>
            </div>
            <div class="swiper-slide">
                <img src="~/Content/Portal/b6bc70cec2b249c2a7a81a95def1960c.png" width="510"/>
            </div>
        </div>
        <!-- Add Pagination -->
        <div class="swiper-pagination"></div>
    </div>
    <script>
        var swiper = new Swiper('.swiper-container', {
            spaceBetween: 30,
            centeredSlides: true,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });
    </script>
</body>
</html>
```