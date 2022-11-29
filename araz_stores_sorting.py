from bs4 import BeautifulSoup
import json

markup = ''' <html lang="azərbaycanca">

<head prefix="og: http://ogp.me/ns#">

    <meta charset="UTF-8">

    <link rel='icon' href='/site/templates/img/favicon.png' type='image/x-icon'/>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>Araz Supermarket Mağazalar | Araz Supermarket</title>

    <link rel="stylesheet" href="/site/templates/css/vendor/bootstrap-grid.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/swiper.min.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/selectric.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/jquery.background-video.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/jquery.fancybox.min.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/normalize.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/datepicker.min.css?v=2">

    <link rel="stylesheet" href="/site/templates/css/style.css?v=1669294084">

    <link rel="stylesheet" href="/site/templates/fonts/stylesheet.css?v=1669294084">

    <link rel="stylesheet" href="/site/templates/css/vendor/fonts.css?v=1669294084">

    <link rel="stylesheet" href="/site/templates/css/additional.css?v=1669294084">

    <link rel="stylesheet" href="/site/templates/css/responsive.css?v=1669294084">





        <meta name="description" content="400-dən çox filialla Araz Supermarketləri sizin xidmətinizdədir.">

    <meta name="keywords" content="araz market unvanlar, araz market unvani, araz supermarket unvanlar, araz market filiallar">

    <meta property="og:type" content="website"/>

    <meta property="og:title" content="Araz Supermarket Mağazalar"/>

    <meta property="og:image" content="https://www.arazmarket.az/site/templates/img/share-logo.jpg"/>

    <meta property="og:image:type" content="image/jpeg" />

    <meta property="og:image:width" content="200"/>

    <meta property="og:image:height" content="200"/>

    <meta property="og:url" content="https://www.arazmarket.az/az/stores/"/>

    <meta property="og:description" content="400-dən çox filialla Araz Supermarketləri sizin xidmətinizdədir."/>

    <meta property="og:keywords" content="araz market unvanlar, araz market unvani, araz supermarket unvanlar, araz market filiallar"/>



    <!-- Google Tag Manager -->

    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':

                new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],

            j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=

            'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);

        })(window,document,'script','dataLayer','GTM-P2ZGV7V');</script>

    <!-- End Google Tag Manager -->





    <!-- Global site tag (gtag.js) - Google Ads: 360230017 -->

    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-360230017"></script>

    <script>

      window.dataLayer = window.dataLayer || [];

      function gtag(){dataLayer.push(arguments);}

      gtag('js', new Date());



      gtag('config', 'AW-360230017');

    </script>





      <!-- Global site tag (gtag.js) - Google Analytics -->

      <script async src="https://www.googletagmanager.com/gtag/js?id=UA-232358221-1"></script>

      <script>

        window.dataLayer = window.dataLayer || [];

        function gtag(){dataLayer.push(arguments);}

        gtag('js', new Date());



        gtag('config', 'UA-232358221-1');

      </script>

      

    <!-- Global site tag (gtag.js) - Google Analytics -->

    <script async src="https://www.googletagmanager.com/gtag/js?id=G-WKD7D0WL7N"></script>

    <script>

      window.dataLayer = window.dataLayer || [];

      function gtag(){dataLayer.push(arguments);}

      gtag('js', new Date());



      gtag('config', 'G-WKD7D0WL7N');

    </script>



</head>

<body class="overflowx-h bg-f5fbff">



<!-- Google Tag Manager (noscript) -->

<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P2ZGV7V" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<!-- End Google Tag Manager (noscript) -->



<!-- Load Facebook SDK for JavaScript -->

<script>

  window.fbAsyncInit = function() {

    FB.init({

      xfbml            : true,

      version          : 'v3.2'

    });

  };



  (function(d, s, id) {

  var js, fjs = d.getElementsByTagName(s)[0];

  if (d.getElementById(id)) return;

  js = d.createElement(s); js.id = id;

  js.src = 'https://connect.facebook.net/en_US/sdk/xfbml.customerchat.js';

  fjs.parentNode.insertBefore(js, fjs);

}(document, 'script', 'facebook-jssdk'));</script>



<!-- Your customer chat code -->

<div class="fb-customerchat"

  attribution=setup_tool

  page_id="498824936833131"

  theme_color="#5bac24"

  logged_in_greeting="Salam! Hər hansı sualınız varsa, buradan yaza bilərsiniz."

  logged_out_greeting="Salam! Hər hansı sualınız varsa, buradan yaza bilərsiniz.">

</div>

<div id="fb-root"></div>

<script>(function(d, s, id) {

  var js, fjs = d.getElementsByTagName(s)[0];

  if (d.getElementById(id)) return;

  js = d.createElement(s); js.id = id;

  js.src = "//connect.facebook.net/az_AZ/sdk.js#xfbml=1&appId=250270611790127&version=v2.0";

  fjs.parentNode.insertBefore(js, fjs);

}(document, 'script', 'facebook-jssdk'));</script>

<script>var switchTo5x=true;</script>



<div id="js-overlay-body" class="overlay fixed d-none opacity-5 bg-black"></div>



<!-- Facebook Pixel Code -->



<script>



!function(f,b,e,v,n,t,s)



{if(f.fbq)return;n=f.fbq=function(){n.callMethod?



n.callMethod.apply(n,arguments):n.queue.push(arguments)};



if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';



n.queue=[];t=b.createElement(e);t.async=!0;



t.src=v;s=b.getElementsByTagName(e)[0];



s.parentNode.insertBefore(t,s)}(window, document,'script',



'https://connect.facebook.net/en_US/fbevents.js');



fbq('init', '366156091916121');



fbq('track', 'PageView');



</script>



<noscript><img height="1" width="1" style="display:none"



src="https://www.facebook.com/tr?id=366156091916121&ev=PageView&noscript=1"





/></noscript>



<!-- End Facebook Pixel Code -->
    <header class="bg-84bf41">
        <section class="container">
            

<div class="bg-84bf41 hover-node header-lg-animate z-100"
     id="js-header">
    <div class="row mx-auto mt-1 my-lg-4 py-3">
        <div class="col-6 col-lg-8 d-flex">
            <a href="/" class="d-inline-block pr-lg-3 pr-xl-3 mr-3">
                <img src="/site/templates/img/icons/logo-white.svg"
                     class="logo-size logo-white obj-contain pos-relative" alt="">
                <img src="/site/templates/img/logo-green.svg" class="logo-size logo-green obj-contain" alt="">
            </a>
            <nav>
                <ul class="d-none d-lg-flex list-reset fs-lg-14 align-items-center">
                                            <li class="pr-3 mr-1">
                            <a href="/az/news/"                                class="underline-0 color-white border-white ">Xəbərlər</a>
                        </li>
                                            <li class="pr-3 mr-1">
                            <a href="/az/araz-musteri-karti/"                                class="underline-0 color-white border-white ">Araz müştəri kartı</a>
                        </li>
                                            <li class="pr-3 mr-1">
                            <a href="/az/blog/"                                class="underline-0 color-white border-white ">Bloq</a>
                        </li>
                                            <li class="pr-3 mr-1">
                            <a href="/az/contacts/"                                class="underline-0 color-white border-white ">Əlaqə</a>
                        </li>
                                            <li class="pr-3 mr-1">
                            <a href="/az/investor-relations/"                                class="underline-0 color-white border-white ">İnvestor münasibətləri</a>
                        </li>
                                    </ul>
                <ul class="d-none d-lg-flex list-reset fw-500 mt-2 pt-1">
                                            <li class="pr-lg-3 pr-xl-4 active-border">
                            <a href="/az/about-us/"                                class="fs-lg-18 underline-0 color-white border-white ">Haqqımızda</a>
                        </li>
                                            <li class="pr-lg-3 pr-xl-4 active-border">
                            <a href="/az/campaigns/"                                class="fs-lg-18 underline-0 color-white border-white ">Kampaniyalar</a>
                        </li>
                                            <li class="pr-lg-3 pr-xl-4 active-border">
                            <a href="/az/stores/"                                class="fs-lg-18 underline-0 color-white border-white active">Mağazalar</a>
                        </li>
                                            <li class="pr-lg-3 pr-xl-4 active-border">
                            <a href="/az/career/"                                class="fs-lg-18 underline-0 color-white border-white ">Karyera</a>
                        </li>
                                    </ul>
            </nav>
        </div>

        <div class="col-6 col-lg-4 d-flex justify-content-end">
            <div class="lang_select">
                <select class="selectric-tooltip label-fs-14" id="js-selectric-lang-footer">
                        <option value="" data-url="/az/stores/" class="d-none">AZ</option><option value="uk" data-url="/en/stores/" >English</option><option value="ru" data-url="/ru/stores/" >Русский</option>                    </select>
            </div>
            <a href="/az/stores/"
               class="d-none d-lg-inline-flex square-40 square-lg-50 bg-white radius-50 mr-1 icon-location bg-center bg-no-repeat"></a>

            <span class="d-flex d-lg-none align-items-center pos-relative">
                <label for="js-selectric-lang-header"
                       class="d-flex square-40 square-lg-50 bg-white radius-50 hover-node border border-transparent cursor-p justify-content-center align-items-center pos-absolute right-0">
                    <span class="icon icon-2x icon-lang bg-center bg-no-repeat"></span>
                </label>

                <select class="selectric-tooltip label-fs-14 opacity-0" id="js-selectric-lang-header">
                    <option value="az" data-url="/az/stores/" class="d-none">AZ</option><option value="uk" data-url="/en/stores/" >English</option><option value="ru" data-url="/ru/stores/" >Русский</option>                </select>
            </span>

            <span class="d-none d-lg-inline-flex radius-8 bg-e7792b text-center align-items-center ml-lg-3 px-4 py-3 cursor-p md-trigger"
                  data-modal="modal-partner">
                <span class="color-white fs-lg-16 fw-500">Partnyor ol</span>
            </span>

            <div class="d-inline-flex d-lg-none align-items-center ml-3 pos-relative">
                <span class="hamburger hamburger--squeeze events-none">
                    <span class="hamburger-box">
                        <span class="hamburger-inner"></span>
                    </span>
                </span>
            </div>
        </div>
    </div>
</div>

<!-- For Mobile Menu -->
<div id="js-menu-mobile"
     class="hover-node bg-white pos-absolute top-0 w-100 z-100 left-100p h-100-vh overflowy-s overflowx-h fixed">
    <div class="d-flex flex-column">
        <div class="row mt-1 py-3 pl-3 border-bottom border-dcdcdc">
            <div class="col-6">
                <a href="/">
                    <figure><img src="/site/templates/img/logo-green.svg" alt=""></figure>
                </a>
            </div>

            <div class="col-6 d-flex align-items-center justify-content-end mt-n2">
                <div class="d-inline-flex align-items-center ml-5 mr-3 pos-relative">
                    <span class="hamburger hamburger--squeeze events-none">
                        <span class="hamburger-box">
                            <span class="hamburger-inner"></span>
                        </span>
                    </span>
                </div>
            </div>
        </div>

        <div class="d-flex flex-column bg-e7ecef py-4">
            <a href="/az/stores/"
               class="d-flex align-items-center fs-16 lh-24 color-262626 p-4 bg-white border-bottom border-dcdcdc">
                <span class="icon icon-location-pin mr-4"></span>
                <span>Mağazalar</span>
            </a>
            <a href="#"
               class="d-flex align-items-center fs-16 lh-24 color-262626 p-4 bg-white border-bottom border-dcdcdc md-trigger"
               data-modal="modal-partner">
                <span class="icon icon-partner mr-4"></span>
                <span>Partnyor ol</span>
            </a>
        </div>

        <div class="d-flex flex-column mb-4">
                            <a href="/az/about-us/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Haqqımızda</a>
                            <a href="/az/campaigns/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Kampaniyalar</a>
                            <a href="/az/stores/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Mağazalar</a>
                            <a href="/az/career/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Karyera</a>
                            <a href="/az/news/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Xəbərlər</a>
                            <a href="/az/araz-musteri-karti/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Araz müştəri kartı</a>
                            <a href="/az/blog/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Bloq</a>
                            <a href="/az/contacts/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">Əlaqə</a>
                            <a href="/az/investor-relations/" class="fs-16 lh-24 color-262626 p-4 border-bottom border-dcdcdc">İnvestor münasibətləri</a>
                    </div>
    </div>
</div>
            <div class="header-content"></div>
        </section>
    </header>

    <section class="color-e7792b bg-white">
        <div class="d-lg-none bg-e7e7e7 py-2 d-none">
            <a href="#" class="d-flex justify-content-center align-items-center color-666 py-1">
                <span class="icon icon-arrow-long rotate-180 icon-color-626262 mr-2"></span>
                <span class="fw-500 fs-13">Geri qayıtmaq</span>
            </a>
        </div>

        <div class="container-fluid pr-lg-0 mr-lg-n5">
            <div class="row">
                <div class="col-lg-4 mt-lg-2">
                    <!--<h1 class="fw-500 fs-25 fs-lg-32 mt-3 mt-5 mb-4"></h1>-->

                    <div class="map_search">
                        <input type="text" placeholder="Filial axtarışı">
                        <a href="javasript:void(0)" class="search_button"></a>
                    </div>

                    <div class="d-flex fs-14 fs-lg-16 lh-lg-24 color-70c21d card-border radius-6 overflowx-h mr-3 overflowx-auto map-filter" id="js-filter-tab">
                         <span class="d-none col text-center cursor-p px-lg-3 py-2 color-84bf41 js-filter-atm events-none shadow bg-84bf41 color-white"
                               data-filter="all"><span class="">Hamısı</span></span>
                                                    <span class="col text-center cursor-p px-lg-3 py-2 color-84bf41 js-filter-atm events-none left-b-ebebeb"
                                  data-filter="1265"><span class="">Superstore</span></span>
                                                    <span class="col text-center cursor-p px-lg-3 py-2 color-84bf41 js-filter-atm events-none left-b-ebebeb"
                                  data-filter="1264"><span class="">Supermarket</span></span>
                                                    <span class="col text-center cursor-p px-lg-3 py-2 color-84bf41 js-filter-atm events-none left-b-ebebeb"
                                  data-filter="1266"><span class="">Mini</span></span>
                                                    <span class="col text-center cursor-p px-lg-3 py-2 color-84bf41 js-filter-atm events-none left-b-ebebeb"
                                  data-filter="1263"><span class="">Express</span></span>
                                                    <span class="col text-center cursor-p px-lg-3 py-2 color-84bf41 js-filter-atm events-none left-b-ebebeb"
                                  data-filter="1376"><span class="">Spar</span></span>
                                            </div>

                    <div class="mt-4 pt-2 scroll-bar" id="js-scroll-map">
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12 shadow mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.424877"
                                             data-lng="49.842583"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Azadlıq Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down slide-up"></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayon, 8 mkr, İbrahimpaşa Dadaşov küçəsi 91</span>

                                        <div class="js-slide-body" >
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-01</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.401577"
                                             data-lng="49.978172"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qaraçuxur Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, A.Alicanov küçəsi 17</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-02</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.413345"
                                             data-lng="49.949493"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Neftçilər Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, Şərifli küçəsi 25</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-03</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.401173"
                                             data-lng="49.831348"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Olimpik Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Mərdanov qardaşları 137</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-04</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.377277"
                                             data-lng="49.810387"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Elmlər Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Şəhriyar küçəsi, 6 nömrəli binanın 1-ci mərtəbəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-05</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.455425"
                                             data-lng="49.740528"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xırdalan-1 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xırdalan şəhəri, Mehdi Hüseynzadə küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00  - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-07</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.362541"
                                             data-lng="49.961208"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xəzər-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Əhmədli qəsəbəsi, Gəncə prospekti</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-08</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.516827"
                                             data-lng="50.102386"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Buzovna-1 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu, Buzovna qəsəbəsi, Heydər Eyvazov küçəsi 47</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-11</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.450150"
                                             data-lng="50.087662"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Binə-1 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu, Binə qəsəbəsi,  Ə.İsazadə küçəsi 5</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-13</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.383633"
                                             data-lng="49.982338"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Günəşli-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxani rayonu, Yeni Günəşli qəsəbəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-14</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.383541"
                                             data-lng="49.823162"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Statistika Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, İnşaatçılar prospekti 31</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-17</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.507488"
                                             data-lng="49.975842"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Savalan Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu rayonu, Maştağa qəsəbəsi, Zabrat - Maştağa şossesinin sağ tərəfində 27 saylı sahə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-16</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.590523"
                                             data-lng="49.674782"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sumqayit-1 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sumqayıt şəhəri, 32-ci məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-18</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.458031"
                                             data-lng="49.756222"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Masazır-1 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Masazır qəsəbəsi, Əliağa Vahid küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-19</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.396942"
                                             data-lng="49.878723"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nərimanov-1 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, 1936-cı məhəllə, Ağa Nemətulla</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-20</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.398094"
                                             data-lng="49.814079"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 20 Yanvar Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Tbilisi prospekti, Alatava 2</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-22</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.390354"
                                             data-lng="49.846695"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar C.Hacıbəyli</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, Bakıxanov k.  məhəllə 758-59</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-23</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.478794"
                                             data-lng="49.753513"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Masazir-2 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Masazır qəsəbəsi, , Əliağa Vahid küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-24</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.392796"
                                             data-lng="49.981812"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qaraçuxur-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Qaraçuxur qəsəbəsi, Yusub Ayvazov küçəsi 2C</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-25</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.423592"
                                             data-lng="49.969093"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bakıxanov-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu rayonu, Bakıxanov qəsəbəsi, Nizami İsmayılov küçəsi, 59 nömrəli  bina</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-27</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.408989"
                                             data-lng="49.867840"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nərimanov-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, Ağa Nemətulla küçəsi,  ev 70a</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-29</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.487041"
                                             data-lng="50.169903"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şüvəlan Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu,  Şüvələn qəsəbəsi,  A.İldırım küçəsi 11 </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-30</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.419823"
                                             data-lng="49.925358"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qarayev-2 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Qara Qarayev prokspekti 1/10</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-32</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.495823"
                                             data-lng="49.855896"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Mehdiabad-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Mehdiabad qəsəbəsi, Fatmai şossesi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-33</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.472164"
                                             data-lng="49.834324"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Binəqədi-1 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, Binəqədi ŞTQ 2-ci mədən</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-36</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.385921"
                                             data-lng="49.808319"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Yasamal 3 Tac Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, H.Zərdabi prospekti, 593-cü məhəllə </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-37</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.360741"
                                             data-lng="50.080055"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Hövsan Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Hövsan qəsəbəsi, İ.Əhlimanov küçəsi 225</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-40</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.511566"
                                             data-lng="49.941521"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Məhəmmədi Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Məhəmmədi kəndi, GöyQurşağı-Məmmədli yaşayış kompleksi, bina1</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-41</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.449623"
                                             data-lng="50.009830"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şuşa-1 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Bülbülə qəsəbəsi, Samir Əliyev küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-43</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.409195"
                                             data-lng="49.844990"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Atatürk Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, A,Salamzadə, ev35V, 1104-cü məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-44</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.448582"
                                             data-lng="50.162071"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qala Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu, Qala qəsəbəsi, 3 saylı Zeytun sovxoz küçəsi, ev 120A</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-47</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.446251"
                                             data-lng="50.089901"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bİnə-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu,  Donuz kökəltmə sovxozu</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-48</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.407032"
                                             data-lng="49.813011"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar 3-cü mkr</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Cavadxan küçəsi 3 MKN 3005-ci məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00  - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-39</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.386482"
                                             data-lng="49.906094"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz NZS Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Rəşid Bağırov küçəsi 25</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-49</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.385040"
                                             data-lng="49.954525"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Əhmədli-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu,  Məhəmməd Hadi küçəsi 41</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-50</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.524120"
                                             data-lng="49.687569"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Saray-1 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Saray qəsəbəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-52</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.388191"
                                             data-lng="49.871136"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xətai-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Babək prospekti, 10 D</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-53</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.380466"
                                             data-lng="49.954262"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Əhmədli-3 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Məhəmməd Hadi küçəsi 51M</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-54</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.402859"
                                             data-lng="49.936935"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Çobanzadə Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, Bəkir Çobanzadə küçəsi 216</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-55</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.421204"
                                             data-lng="49.809101"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 9-cu mkr-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, 9 mkr, H.Seyidzadə küçəsi 38</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-56</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.367928"
                                             data-lng="49.827564"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar Axundov</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Səbail rayonu, B.Sərdarov küçəsi 15</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-57</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.419670"
                                             data-lng="49.931591"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qarayev-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, Tofiq Abbasov küçəsi 38, bina 7</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-59</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.405621"
                                             data-lng="49.955521"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 8-ci km-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, C.Naxçıvanski küçəsi 66 A, giriş 1 və 2</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-62</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.409245"
                                             data-lng="49.952496"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 8-ci km-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, E.Süleymanov 2566 blok-B, mərtəbə 1</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-63</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.364113"
                                             data-lng="50.073154"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Hövsan-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Hövsan Qəsəbəsi, Elman Qasıməv küçəsi 227 A</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-64</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.415562"
                                             data-lng="49.828979"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Cəfər Xəndan Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, M.Ə.Rəsulzadə qəsəbəsi, Cəfər Xəndan küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-69</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.350906"
                                             data-lng="49.810612"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Badamdar-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Səbail rayonu, Badamdar qəsəbəsi, 1 yaşayış massivi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-66</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.393955"
                                             data-lng="49.815659"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şəfayət Mehdiyev Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Ə.Ələkbərov küçəsi 1054 - cü məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-68</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.381950"
                                             data-lng="49.804306"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şərifzadə Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Bakı şəhəri, Şərfizadə küçəsi ünvanı</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-67</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.418156"
                                             data-lng="49.933064"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qarayev-4 Express</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, Qara Qarayev prospekti 25A </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-72</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.441345"
                                             data-lng="49.771458"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xırdalan-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Xırdalan şəhəri, H.Əliyev prospekti 7</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-70</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.426498"
                                             data-lng="49.827896"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 6-cı mkr Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, 6-cı mkr, İ.Haşımov küçəsi 1 A </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-74</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.381153"
                                             data-lng="49.834560"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Ə.Hüseynzadə Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Ə.Hüseynzadə küçəsi 84</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-78</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.362541"
                                             data-lng="49.961208"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xəzər-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Gəncə prospekti 2942 "Q" məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-77</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.519325"
                                             data-lng="50.095387"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Buzovna-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Buzovna qəsəbəsi, Buzovna-Maştağa yolunun sağ tərəfi, Zagulba yolu</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-83</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.388119"
                                             data-lng="49.845379"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Mirəli Qaşqay Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Kavoreçkin küçəsi ilə Mirəli Qaşqay küçəsinin kəsişməsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-88</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.374855"
                                             data-lng="49.841648"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar Tarqoviy</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Səməd Vurğun küçəsi 19</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-94</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.375843"
                                             data-lng="49.811668"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Elmlər-3 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Firudin Ağayev 9 </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-95</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.398582"
                                             data-lng="49.859413"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar Gənclik</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, 865 - ci məhəllə, Koroğlu Rəhimov küçəsi 22C (ABU arenanın qarşısı)</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-96</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.382133"
                                             data-lng="49.807125"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Yasamal-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, M.Seyidov küçəsi 41E, 3148-ci məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-10</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="41.629333"
                                             data-lng="46.634918"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Zaqatala Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Zaqatala rayonu, Faiq Əmirov küçəsi 25 (Zaqatala mall)</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-498-83-83</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="39.867607"
                                             data-lng="48.060246"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz İmişli Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">İmişli rayonu, İmişli şəhəri, Baki küçəsi ev 44</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-99</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.570278"
                                             data-lng="49.689060"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sumqayıt-3 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sumqayıt şəhəri, 9-cu mkr, Üzeyir Hacıbəyov küçəsi 25C</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-79</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.383804"
                                             data-lng="49.861237"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xətai 2 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Həsən Salmani küçəsi 17</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-18</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.402458"
                                             data-lng="49.950615"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xalqlar Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, Q.Qarayev prospekti 93 L</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-19</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.458031"
                                             data-lng="49.756222"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Masazır-3 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Masazır qəsəbəsi, Bakı-Sumqayıt yolu</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-515-85-09</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.377731"
                                             data-lng="49.852070"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar 28 May Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Səməd Vurğun küçəsi 50</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-21</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.402119"
                                             data-lng="49.874187"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nərimanov-3 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, N.Hacıyev və F.Yusifov küçəsinin kəsişməsi, 1950-ci məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-20</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.410172"
                                             data-lng="49.814663"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar Memar Əcəmi Express</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, 5-ci mkr, Cavadxan küçəsi, 3005-ci məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-22</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.368992"
                                             data-lng="49.975765"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Günəşli-2 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Yeni Günəşli D yaşayış sahəsi, 26-cı bina</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-24</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.348434"
                                             data-lng="49.998703"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qum adası Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Zığ-Hövsan şossesi, Qum adası yolu</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-25</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.523682"
                                             data-lng="50.099937"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Buzovna-3 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu, Zaqulba qəsəbəsi, R.İmanov küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-28</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.432804"
                                             data-lng="49.850559"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 7-ci mkr Express</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, 7 mkr, 3123-cü məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-26</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.368496"
                                             data-lng="49.830379"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar Axundov Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Səbail rayonu, 129-cu məhəllə,  Əhməd Cavad küçəsi 3</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-37</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.425941"
                                             data-lng="49.830589"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 6-cı mkr Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, 6-cı mkr, Svetlana Məmmədova küçəsi 209 F</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-38</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.566978"
                                             data-lng="49.685425"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sumqayıt-5 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sumqayıt şəhəri, 9-cu mkr Ü.Hacıbəyov və Koroğlu küçələrinin kəsişməsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-32</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.523411"
                                             data-lng="46.082630"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Daşkəsən Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Daşkəsən şəhəri, Nizami küç. 14</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-34</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.675087"
                                             data-lng="46.334614"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Gəncə-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Gəncə şəhəri, Yeni Gəncə qəsəbəsi, Ə.Mehmandarov küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-36</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="39.927883"
                                             data-lng="48.358940"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Saatlı Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Saatlı şəhəri, H.Əliyev pr. 240</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-35</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.497093"
                                             data-lng="49.949776"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Məhəmmədi-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Zabrat dairəsi, Məhəmmədi kəndi istiqaməti</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-39</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.428905"
                                             data-lng="49.852238"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 7-ci mkr-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, F.Məlikov küçəsi 18A</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-40</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.390038"
                                             data-lng="49.958344"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Əhmədli 5 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Q.Nəbi küçəsi 5 saylı bina</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-45</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.398041"
                                             data-lng="49.839874"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz N.Yusifbəyli Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Nəsib bəy Yusifbəyli küçəsi 94</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-42</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.224918"
                                             data-lng="49.572365"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sahil Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Qaradağ rayonu, Sahil qəsəbəsi, Məhərrəm Seyidov küçəsi 15</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-46</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.428715"
                                             data-lng="49.962269"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bakıxanov-4 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu rayonu, Bakıxanov qəsəbəsi, N.İsmayılov küçəsi 15</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-48</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.436199"
                                             data-lng="49.803444"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Biləcəri Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, Biləcəri qəsəbəsi, M.Hüseyn küçəsi 17</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-50</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.406391"
                                             data-lng="49.938370"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Neftçilər-2 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, R.Rüstəmov küçəsi 12c</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-49</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.372826"
                                             data-lng="49.954556"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Həzi Aslanov Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, M.Hadi küçəsi 73A</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-53</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.487946"
                                             data-lng="49.854427"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Mehdiabad-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Mehdiabad qəsəbəsi, 28 May küçəsi (Mehdiabad ticarət mərkəzinin 1-ci mərtəbəsi)</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-52</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.436218"
                                             data-lng="49.862823"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar Rəsulzadə</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, M.Ə.Rəsulzadə qəsəbəsi, Binəqədi şosesi </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-54</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.457169"
                                             data-lng="49.722996"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xırdalan-3 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xırdalan şəh., AAAF Park yaşayış kompleksi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-58</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1376">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-spar square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.380623"
                                             data-lng="49.857449"
                                             data-icon="map-spar">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-db4044">Spar Çay fabriki</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-248d50 radius-6">Spar</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, D.Əliyeva küç. 253</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-59</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.426880"
                                             data-lng="49.849480"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 7-ci mkr-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi ray., 7-ci mkr, S.S.Axundov küç. 3C</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-60</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.444942"
                                             data-lng="49.943359"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sabunçu Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu qəs., Ə.Məmmədəliyev küç. 18A (Sabunçu xəstəxanasının yaxınlığı)</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-57</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.771084"
                                             data-lng="47.041107"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Mingəçevir Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Mingəçevir şəhəri, Heydər Əliyev prospekti</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-62</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.543705"
                                             data-lng="49.663124"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Ceyranbatan Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Ceyranbatan qəsəbəsi, Bakı-Sumqayıt şossesi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-63</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.476822"
                                             data-lng="49.938290"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Zabrat Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Zabrat qəsəbəsi, Neftçilər küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-56</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.385021"
                                             data-lng="49.971889"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Günəşli-3 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Günəşli qəsəbəsi, Babək prospekti, Qartal heykəlinin qarşısı</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-61</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.432659"
                                             data-lng="50.033588"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Suraxanı Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Yeni Suraxanı ŞTQ 14 iyul ev. 24</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 400 85 76</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.377922"
                                             data-lng="49.832870"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nizami Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, 422-ci məhəllə, Mirzə İbrahimov küçəsi 53, 1-ci mərtəbə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 252 26 07</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.547504"
                                             data-lng="49.911598"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Kürdəxanı Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Kürdəxanı qəsəbəsi, Əjdər Məlikov küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 215 12 89</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.401096"
                                             data-lng="49.837719"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Azadlıq-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, məhəllə 944. S. Rüstəmov küç.. ev 41</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-12</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.401550"
                                             data-lng="49.839767"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz İnqilab Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu. Akademik Mirəli Qaşqay küçəsi. ev 94. 1-ci mərtəbə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-13</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.371037"
                                             data-lng="49.818111"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Elmlər Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu. Ə. Ələkbərov küç. 510</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 400 85 02</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.366989"
                                             data-lng="49.815624"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Space Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Hüseyn Cavid prospekti 17</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-09</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.380329"
                                             data-lng="49.811092"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Yasamal Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu. Ə. Haqverdiyev küçəsi. məhəllə 574</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-10</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.383720"
                                             data-lng="49.826378"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Statistika-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu. M. H. Naxçıvani 15</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-04</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.412628"
                                             data-lng="49.933979"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Planet Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu. M. Abbasov 50 B</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-15</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.430744"
                                             data-lng="49.850845"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 7-ci mkr-4 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, 7-ci mkr, Xarici Dairəvi küçəsi bina 22 blok 1</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-01</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.436234"
                                             data-lng="49.844860"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Rəsulzadə Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, M.Ə.Rəsulzadə qəsəbəsi, Azadlıq prospekti 157</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-11</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.466389"
                                             data-lng="49.829311"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Binəqədi Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, Gülməmməd Ramazanov küçəsi, (1 sayli qarışıq mallar mağazasi) 2-ci mədən, korpus 52</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 400 85 05</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.418823"
                                             data-lng="49.811012"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 9-cu mkr Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, 9-cu mikrorayon, Mir Cəlal küçəsi 59 K</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00  - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-14</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.383411"
                                             data-lng="49.966640"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Neapol Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, General Şıxlınski küçəsi 55</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 400 85 03</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.367821"
                                             data-lng="49.959778"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xəzər-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Gəncə prospekti, 2942 saylı məhəllə, korpus 3</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-06</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.330032"
                                             data-lng="49.818501"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bayıl Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Səbail rayonu, Salyan şössesi, 20-ci ünvan</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-08</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.537113"
                                             data-lng="49.783222"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Novxanı Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Novxanı kəndi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-16</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="41.362682"
                                             data-lng="48.522152"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Quba Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Quba rayonu, Heydər Əliyev pr.</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-400-85-07</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.386673"
                                             data-lng="49.982624"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Yeni Günəşli-4 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address"> Suraxanı rayonu, Samir Cəfərov, ev2, V massivi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 864 95 30</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.394840"
                                             data-lng="49.796425"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Yeni Yasamal-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Yeni Yasamal 1, ev 1H</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 202 65 24</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.338688"
                                             data-lng="49.807571"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Badamdar-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Səbail rayonu, Badamdar qəsəbəsi, Tofiq Məmmədov </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 202 65 46</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.406013"
                                             data-lng="49.811314"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Yanvar 20-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Məmmədcəfər Cəfərov küçəsi, 3006 məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 201 83 73</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.378197"
                                             data-lng="49.807732"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Yeni Yasamal Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Mirəli Seyidov küçəsi 23</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 400 85 87</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.576138"
                                             data-lng="49.669239"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sumqayıt-6 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sumqayıt şəhəri, Koroğlu küçəsi, 41-ci məhəllə, Koroğlu prospekti</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 226 51 10</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.547703"
                                             data-lng="49.712955"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Saray-2 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Saray qəsəbəsi, Məhəmməd Əsədov küçəsi, 68-ci binanın birinci mərtəbəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 400 85 79</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.459122"
                                             data-lng="49.744308"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xırdalan-4 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xırdalan şəhəri, Nizami Gəncəvi küçəsi, 1-ci mərtəbə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 414 24 74</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.403919"
                                             data-lng="49.877850"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nərimanov-4 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, Ə.Əliyev küçəsi, 26-cı məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 226 51 12</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.376137"
                                             data-lng="49.960976"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz N.Tusi Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, N.Tusi küçəsi 19</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 300 83 77</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.389351"
                                             data-lng="49.857647"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qarabağ Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, Qarabağ küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 256 78 20</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.408443"
                                             data-lng="49.958000"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 8-ci km-4 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, Cəmşid Naxçivanı küçəsi 90 nömrəli binanın 1-ci mərtəbəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 500 74 67</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.446709"
                                             data-lng="50.089024"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Binə-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu, Binə qəsəbəsi, Hövsan Südçülük sovxozuna gedən yolun sağ tərəfi  </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 525 30 15</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.383377"
                                             data-lng="49.974869"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Günəşli-5 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Günəşli qəsəbəsi, AB massivi 127</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 500 97 76</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.385242"
                                             data-lng="49.844257"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Azadlıq-2 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nəsimi rayonu, Azadlıq prospekti 103</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 08 11</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.402145"
                                             data-lng="49.955322"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 8-ci km-5 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, B.Nuriyev küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 67 88</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.555054"
                                             data-lng="50.022453"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bilgəh Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu rayonu, Nardaran qəsəbəsi, 9 Z saylı ərazi </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 67 89</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.509075"
                                             data-lng="49.915836"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Məhəmmədi-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Məhəmmədi kəndi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 67 25</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.360977"
                                             data-lng="50.077820"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Hövsan-3 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Hövsan qəsəbəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 67 23</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.416039"
                                             data-lng="49.964676"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bakıxanov-5 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu rayonu, Bakıxanov qəsəbəsi, Sakit Qocayev küçəsi 35</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 67 26</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.400349"
                                             data-lng="49.870441"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nərimanov-5  Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, M.Məmmədzadə/Ə.Orucəliyev/N.Hacıyev küçələrinin kəsişməsində</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 67 42</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.433952"
                                             data-lng="49.773163"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sulutəpə-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, Sulutəpə qəsəbəsi, Ruslan Allahverdiyev küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 400 85 29</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.367275"
                                             data-lng="49.941563"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nargilə-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Zığ şossesi 8, blok 1, 1-ci mərtəbə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 500 61 35</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.432625"
                                             data-lng="49.771278"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sulutəpə-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, Sulutəpə qəsəbəsi, R.Allahverdiyev küçəsi, ev 25F   </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 300 83 90</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.332138"
                                             data-lng="49.802826"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Badamdar-3 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Badamdar qəsəbəsi, 22-ci küçə, 3-cü massiv </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 515 85 21</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.358704"
                                             data-lng="50.067162"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Hövsan-4 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Hövsan qəsəbəsi, Oqtay Şabanov küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 515 85 58</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.688095"
                                             data-lng="46.352371"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Gəncə-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Gəncə şəhəri, Şəddadilər küçəsi 108</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 08 83</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.417198"
                                             data-lng="49.838631"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 8-ci mkr-2 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, Cəfər Xəndan küçəsi 150 (Tərgül ticarət mərkəzi)</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 67 47</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.470043"
                                             data-lng="49.742256"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Abşeron-1 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xırdalan şəhəri, Abşeron Gənclər şəhərciyi, Sumqayıt şossesi 7 (Riyad ticarət mərkəzi ilə üzbəüz) </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 15</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.394524"
                                             data-lng="49.950237"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Əhmədli-6 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nizami rayonu, Babək prospekti 64</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 60</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.477703"
                                             data-lng="49.987919"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Ramana-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu rayonu, Ramana qəsəbəsi, E.Məhərrəmli küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 25</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.372177"
                                             data-lng="49.820423"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qutqaşınlı-1 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, İ.Qutqaşınlı küç 85</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 26</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.491539"
                                             data-lng="49.855244"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Mehdiabad-3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Mehdiabad qəs. Novruz küçəsi ev 1</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 02:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 65</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.460838"
                                             data-lng="49.741203"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xirdalan-5 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xırdalan şəhəri, Nizami Gəncəvi küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 46</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.396263"
                                             data-lng="49.875515"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nərimanov-8 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, Ə. Orucəliyev küçəsi 7</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 44</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="41.200283"
                                             data-lng="47.177299"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şəki Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Şəki şəhəri, M.Ə.Rəsulzadə pr 169</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 64</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.394402"
                                             data-lng="49.875912"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nərimanov-6 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, Çaykovski küçəsi 10</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 93</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.561623"
                                             data-lng="49.694092"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sumqayıt-7 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sumqayıt şəhəri, Koroğlu küçəsi 395, 10-cu mkr</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 90</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.071949"
                                             data-lng="49.411850"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Qobustan Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Qobustan qəsəbəsi, Bakı - Ələt yolunun 58-ci km-liyi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 05</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.569878"
                                             data-lng="49.675194"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sumqayıt-8 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sumqayıt şəhəri, 11-ci mikrorayon, Bədəlbəyli küçəsi 34A</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">24\7</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 04</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.364113"
                                             data-lng="50.073154"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Hövsan 2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Suraxanı rayonu, Hövsan qəsəbəsi, Elman Qasımov küçəsi 227 A</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:30 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 515 85 64</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.607880"
                                             data-lng="47.149147"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Yevlax Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yevlax şəhəri, Məhəmməd Füzuli küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 40</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.484329"
                                             data-lng="49.756336"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Masazır 5 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Masazır qəsəbəsi, Əliağa Vahid küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 96 44</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="39.762844"
                                             data-lng="46.748207"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şuşa şəhəri Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Şuşa şəhəri, 20 Yanvar küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 20:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 06</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.360359"
                                             data-lng="49.946903"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Nargilə 3 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Zığ yolu 31A, blok 3.</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 204 96 47</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1265">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.416225"
                                             data-lng="49.968266"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bakıxanov-6 Superstore</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Superstore</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Muxtar Fətəliyev küçəsi 151 A</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 13</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.394569"
                                             data-lng="49.952446"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Əhmədli 7 Express</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Əhmədli qəsəbəsi, M.Hadi küçəsi, 2341-2343-cü məhəllə, ev 2 </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 83 09</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.387386"
                                             data-lng="49.787609"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Yeni Yasamal-2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Əsəd Əhmədov küçəsi 9, döngə 5</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 28 20</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.369431"
                                             data-lng="49.962055"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Tusi 2 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Nəsrəddin Tusi 45</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 83 29</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.491493"
                                             data-lng="49.746567"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Masazır-4 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Masazır qəsəbəsi, Yeni Bakı yaşayış kompleksi, ev 6</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 44</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.432434"
                                             data-lng="49.804684"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Biləcəri 3 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address"> Binəqədi rayonu, Biləcəri qəsəbəsi, Yahya Hüseynov küçəsi 33 c</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 83 99</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.366039"
                                             data-lng="49.955395"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Həzi Aslanov-2 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, M.Hadi küçəsi, 2942 A məhəllə        </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 89</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.417709"
                                             data-lng="50.107887"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Binə 4 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xəzər rayonu, Binə qəsəbəsi, Vaqif küçəsi, Hövsan südçülük savxozu, ev 71</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 34</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.446800"
                                             data-lng="49.797108"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Biləcəri-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Biləcəri qəsəbəsi, Biləcəri-Binəqədi dairəvi yolu  </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 88</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.410492"
                                             data-lng="49.843937"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Atatürk 2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Nərimanov rayonu, İ.Dadaşov küçəsi 57 X     </span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 83 25</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.496326"
                                             data-lng="50.198189"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şüvəlan-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Şüvəlan qəsəbəsi, Lev Starçuk küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 93</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.412827"
                                             data-lng="49.813202"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz M. Əcəmi 2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Bakı şəhəri , Nəsimi rayonu 3-cü mkr , Cavadxan küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 200 83 29</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.769966"
                                             data-lng="46.998623"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Minəçevir-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Mingəçevir şəhəri, Naxçıvan küçəsi ev 42 B</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 204 96 05</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.562477"
                                             data-lng="49.684307"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Sumqayıt-9 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sumqayıt şəhəri, 12-ci mkr, Çerkassi küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 900 36 90</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.446938"
                                             data-lng="49.751148"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xırdalan-6 Supermarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xırdalan şəhəri, Heydər Əliyev prospekti 11</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">07:00 - 23:00</span>
                                                                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.475517"
                                             data-lng="49.948154"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Zabrat-2 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Sabunçu rayonu, Zabrat qəsəbəsi, R. Axundov küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-333-37-81</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.420235"
                                             data-lng="49.839996"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz 8-ci mkr-3 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, 8-ci mikrorayon, Nizami Nərimanov küçəsi, 3078-ci məhəllə</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 333 43 18</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1263">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.497898"
                                             data-lng="49.851330"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Mehdiabad-4 Ekspress</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Express</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Abşeron rayonu, Mehdiabad qəsəbəsi, Cəfər Cabbarlı küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 333 47 25</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.444790"
                                             data-lng="49.809513"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Biləcəri-5 Minimarket</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Binəqədi rayonu, Biləcəri qəsəbəsi, 3-cü yeni Y/M, Xudayat Məlikaslanov küçəsi 36</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 00:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 333 43 80</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.343227"
                                             data-lng="49.838390"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Bayıl-2</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Bakı şəh. Səbail rayonu , Bayıl qəsəbəsi Xanlar küçəsi 119</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 333 47 31</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1264">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.441151"
                                             data-lng="49.763580"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Xırdalan-7</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Supermarket</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xırdalan şəhəri Heydər Əliyev Prospekti 95</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055-333-46-22</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.391510"
                                             data-lng="49.802345"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Şərifzadə-2</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Yasamal rayonu, Abbas Mirzə Şərifzadə küçəsi</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                    <span class="fs-13 color-9f9f9f mb-2">Telefon</span>
                                                    <span class="fs-15 mb-4 mb-lg-2 opacity-8">055 333 57 28</span>
                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                                    <div class="color-262626">
                                <div class="d-flex p-3 p-lg-4 border-028 radius-12  mb-3 mr-2 hover-node js-slide" data-category="1266">
                                    <div class="pr-4">
                                <span class="d-inline-flex radius-50 align-items-center justify-content-center bg-84bf41">
                                    <span class="icon icon-a-bg square-40"></span>
                                </span>
                                    </div>

                                    <div class="flex-fill">
                                        <div class="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none"
                                             data-lat="40.379681"
                                             data-lng="49.965164"
                                             data-icon="map">
                                            <div>
                                                <h4 class="fw-500 fs-16 mt-0 mb-2 color-84bf41">Araz Neapol-2</h4>
                                                                                                    <span class="d-inline-flex fs-12 color-white px-3 py-1 bg-e7792b radius-6">Mini</span>
                                                                                            </div>
                                            <span class="icon icon-2x mt-n3 slide-down "></span>
                                        </div>

                                        <span class="color-black d-block fs-14 lh-18 mb-1 opacity-8 js-address">Xətai rayonu, Əhmədli qəsəbəsi, General Əliağa Şıxlinski küç. 03</span>

                                        <div class="js-slide-body" style="display: none">
                                            <div class="d-flex flex-column">
                                                                                                    <span class="fs-13 color-9f9f9f mb-2 pt-3">İş vaxtı</span>
                                                    <span class="fs-14 lh-18 mb-3 opacity-8">08:00 - 23:00</span>
                                                                                                                                                <span class="d-lg-none btn bg-e7792b color-white col js-slide-button">Xəritədə bax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                            </div>
                </div>

                <div class="col-lg-8 px-0 pl-lg-4 pr-lg-3 d-flex fixed pos-lg-static top-0 left-100p hover-node z-10"
                     id="js-map-block">
                    <div>
                        <!-- mobile -->
                        <div class="d-flex d-lg-none map-close align-items-center bg-white close-ios-map">
                            <span class="cursor-p fs-15 fs-lg-13 mr-2 pr-lg-1 fw-600">Xəritəni bağla</span>
                            <span class="icon square-12 icon-close icon-color-e7792b"></span>
                        </div>

                        <!-- desktop -->
                        <div class="d-none d-lg-flex color-262626 map-close radius-3">
                            <div class="d-inline-flex fs-14 fs-lg-16 lh-lg-24 color-70c21d card-border radius-6 bg-white overflowx-h border-028 shadow">
                                <a href="#" class="d-flex align-items-center px-3 px-lg-4 py-3 events-none"
                                   id="js-map-prev" data-index="0">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="20" viewBox="0 0 13 20">
                                        <path fill="none" fill-rule="evenodd" stroke="#E7792B" stroke-linecap="round"
                                              stroke-linejoin="round" stroke-width="3" d="M28 25L37 33 28 41"
                                              transform="matrix(-1 0 0 1 39 -23)"></path>
                                    </svg>
                                </a>

                                <a href="#"
                                   class="d-flex align-items-center px-3 px-lg-4 py-3 events-none left-b-ebebeb"
                                   id="js-map-next" data-index="1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="20" viewBox="0 0 13 20">
                                        <path fill="none" fill-rule="evenodd" stroke="#E7792B" stroke-linecap="round"
                                              stroke-linejoin="round" stroke-width="3" d="M110 25L119 33 110 41"
                                              transform="translate(-108 -23)"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>

                        <span class="map-gradient d-none d-lg-none"></span>
                    </div>

                    <div id="js-map-canvas" class="map-canvas"></div>
                </div>
            </div>
        </div>
    </section>


<div class="md-modal md-effect-14" id="modal-partner">

    <div class="md-content">

        <div class="container pt-5 mt-5 pt-lg-0 mt-lg-0">
    <div class="row">
        <div class="col-lg-12">

            <div class="row bg-white border-028 p-3 p-lg-5 radius-20">
                <h3 class="col-12 text-center fs-24 fs-lg-38 color-e7792b fw-500 mt-0 mb-4 mb-lg-5 d-flex align-items-center justify-content-between">
                    <span class="flex-fill">Partnyor ol</span>
                    <span class="md-close cursor-p d-inline-flex align-items-center justify-content-center circle-65 square-40 square-lg-65 bg-white pos-absolute pos-lg-static right-0 mt-n5 mt-lg-0"
                          style="top: -25px">
                        <span class="icon square-lg-20 icon-close icon-color-e7792b"></span>
                    </span>
                </h3>

                                <div class="row text-center">
                                            <div class="col-lg-4 mb-4 color-black cursor-p events-none js-partner">
                            <div class="border-028 radius-10 p-3 p-lg-4">
                                <div class="icon square-36 mt-3 icon-offer-facility"></div>
                                <h4 class="fs-16 fs-lg-20 fw-500 mb-3">Obyekt təklifi</h4>
                                <p class="fs-12 fs-lg-14 lh-21 opacity-5">Zəhmət olmasa müraciətinizi təsvir edin və imkanlarınız barədə məlumat verin</p>
                            </div>
                        </div>
                                            <div class="col-lg-4 mb-4 color-black cursor-p events-none js-partner">
                            <div class="border-028 radius-10 p-3 p-lg-4">
                                <div class="icon square-36 mt-3 icon-offer-product"></div>
                                <h4 class="fs-16 fs-lg-20 fw-500 mb-3">Məhsul təklifi</h4>
                                <p class="fs-12 fs-lg-14 lh-21 opacity-5">Zəhmət olmasa müraciətinizi təsvir edin və imkanlarınız barədə məlumat verin</p>
                            </div>
                        </div>
                                            <div class="col-lg-4 mb-4 color-black cursor-p events-none js-partner">
                            <div class="border-028 radius-10 p-3 p-lg-4">
                                <div class="icon square-36 mt-3 icon-offer-a"></div>
                                <h4 class="fs-16 fs-lg-20 fw-500 mb-3">Françayzinq</h4>
                                <p class="fs-12 fs-lg-14 lh-21 opacity-5">Zəhmət olmasa müraciətinizi təsvir edin və imkanlarınız barədə məlumat verin</p>
                            </div>
                        </div>
                                    </div>

                <!-- forms -->
                <div class="col-12 color-black" style="display: none" id="js-partner-choose">
                    <div class="row color-black border-028 radius-10 text-center">
                                                    <div class="col-lg-4 border-right-short cursor-p events-none partner-tab "
                                 data-tab="tab-0" data-tab-container="tab-forms">
                                <h4 class="d-flex align-items-center justify-content-center my-3">
                                    <span class="icon icon-2x mr-3 icon-offer-facility"></span>
                                    <span class="fs-16 fs-lg-17 lh-25">Obyekt təklifi</span>
                                </h4>
                            </div>
                                                    <div class="col-lg-4 border-right-short cursor-p events-none partner-tab "
                                 data-tab="tab-1" data-tab-container="tab-forms">
                                <h4 class="d-flex align-items-center justify-content-center my-3">
                                    <span class="icon icon-2x mr-3 icon-offer-product"></span>
                                    <span class="fs-16 fs-lg-17 lh-25">Məhsul təklifi</span>
                                </h4>
                            </div>
                                                    <div class="col-lg-4 border-right-short cursor-p events-none partner-tab last"
                                 data-tab="tab-2" data-tab-container="tab-forms">
                                <h4 class="d-flex align-items-center justify-content-center my-3">
                                    <span class="icon icon-2x mr-3 icon-offer-a"></span>
                                    <span class="fs-16 fs-lg-17 lh-25">Françayzinq</span>
                                </h4>
                            </div>
                                            </div>

                    <!-- Forms -->
                    <div class="row mt-5">
                        <!-- Facility -->
                        <form id="tab-0" class="js-ajax tab-forms w-100 js-parsley-validate"
                              data-parsley-trigger="change input" data-url="">
                            <div class="row">
                                <label class="col-12 mb-4 d-flex align-items-center">
                                    <input name="fullname" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60 mask_letter"
                                           placeholder="Tam ad" maxlength="40">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="email" type="email" required
                                           class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="E-mail" maxlength="40">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="phone" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60 mask_phone"
                                           placeholder="Mobil nömrə">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="address" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="Obyektin ünvanı" maxlength="50">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="area" type="number" required
                                           class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="Obyektin sahəsi ( kv/m )">
                                </label>


                                <label class="col-12 mb-3 mb-lg-4 d-flex align-items-center">
                                    <textarea name="message" required
                                              class="form-input px-3 px-lg-4 h-140 py-3 resize-none"
                                              placeholder="Zəhmət olmasa müraciətinizi təsvir edin və imkanlarınız barədə məlumat verin"  maxlength="250"></textarea>
                                </label>

                                <label class="col-lg-6 d-flex align-items-center mx-auto mt-2">
                                    <input type="hidden" name="form" value="FormPlace"/>
                                    <input type="submit" class="form form-input h-lg-60 bg-e7792b color-white cursor-p"
                                           value="Sorğu göndər">
                                </label>
                            </div>
                            

                <script>function onClick(e) {e.preventDefault();grecaptcha.ready(function () {grecaptcha.execute('6LfLXAEVAAAAAFyiXA9lf25xbR-8Rrlym1boAKZy', {action: 'submit'}).then(function (token) {});});}</script>



                                        </form>

                        <!-- Product -->
                        <form id="tab-1" class="js-ajax tab-forms w-100 js-parsley-validate"
                              data-parsley-trigger="change input" data-url="">
                            <div class="row">
                                <label class="col-12 mb-4 d-flex align-items-center">
                                    <input name="fullname" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60 mask_letter"
                                           placeholder="Tam ad" maxlength="40">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="email" type="email" required
                                           class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="E-mail" maxlength="40">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="phone" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60 mask_phone"
                                           placeholder="Mobil nömrə">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="product" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="Məhsulun növü" maxlength="50">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="address" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="Obyektin ünvanı" maxlength="50">
                                </label>

                                <label class="col-12 mb-3 mb-lg-4 d-flex align-items-center">
                                    <textarea name="message" required
                                              class="form-input px-3 px-lg-4 h-140 py-3 resize-none"
                                              placeholder="Zəhmət olmasa müraciətinizi təsvir edin və imkanlarınız barədə məlumat verin"  maxlength="250"></textarea>
                                </label>

                                <label class="col-lg-6 d-flex align-items-center mx-auto mt-2">
                                    <input type="hidden" name="form" value="FormProduct"/>
                                    <input type="submit" class="form form-input h-lg-60 bg-e7792b color-white cursor-p"
                                           value="Sorğu göndər">
                                </label>
                            </div>
                            

                <script>function onClick(e) {e.preventDefault();grecaptcha.ready(function () {grecaptcha.execute('6LfLXAEVAAAAAFyiXA9lf25xbR-8Rrlym1boAKZy', {action: 'submit'}).then(function (token) {});});}</script>



                                        </form>

                        <!-- Franchising -->
                        <form id="tab-2" class="js-ajax tab-forms w-100 js-parsley-validate"
                              data-parsley-trigger="change input" data-url="">
                            <div class="row">
                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="fullname" type="text" required class="form-input px-3 px-lg-4 h-lg-60 mask_letter"
                                           placeholder="Tam ad" maxlength="40">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="store" type="text" required class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="Hal-hazırda fəaliyyət göstərən mağazanına adı" maxlength="50">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="email" type="email" required class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="E-mail" maxlength="40">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="phone" type="text" required
                                           class="form-input px-3 px-lg-4 h-lg-60 mask_phone"
                                           placeholder="Mobil nömrə" >
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="address" type="text" required class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="Obyektin ünvanı" maxlength="50">
                                </label>

                                <label class="col-lg-6 mb-4 d-flex align-items-center">
                                    <input name="area" type="number" required class="form-input px-3 px-lg-4 h-lg-60"
                                           placeholder="Obyektin sahəsi ( kv/m )">
                                </label>


                                <label class="col-12 mb-3 mb-lg-4 d-flex align-items-center">
                                    <textarea name="message" required
                                              class="form-input px-3 px-lg-4 h-140 py-3 resize-none"
                                              placeholder="Zəhmət olmasa müraciətinizi təsvir edin və imkanlarınız barədə məlumat verin" maxlength="250"></textarea>
                                </label>

                                <label class="col-lg-6 d-flex align-items-center mx-auto mt-2">
                                    <input type="hidden" name="form" value="FormFranchise"/>
                                    <input type="submit" class="form form-input h-lg-60 bg-e7792b color-white cursor-p"
                                           value="Sorğu göndər">
                                </label>
                            </div>
                            <div class="my_captcha" data-key="6LdUczceAAAAAPNZa0AJFbabwkXN6Rm7jlx_dRTj"></div>
                            <script src="https://www.google.com/recaptcha/api.js?render=6LdUczceAAAAAPNZa0AJFbabwkXN6Rm7jlx_dRTj"></script>
                        </form>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>    </div>

</div>





<div class="md-trigger d-none" id="js-modal-success" data-modal="modal-success"></div>

<div class="md-modal md-effect-14" id="modal-success" style="top: 40%">

    <div class="md-content">

        <div class="container">

            <section class="row">

                <div class="col-lg-8 mx-auto">

                    <div class="row no-gutters radius-20 bg-white">

                        <div class="col-lg-12 p-4 d-flex">

                            <span class="icon icon-success square-48 mr-4 pr-3"></span>

                            <div class="flex-fill">

                                <p class="color-black fs-20 lh-24 m-0"></p>

                                <p class="color-black fs-14 lh-20 mb-0"></p>

                            </div>

                        </div>

                    </div>

                </div>

            </section>

        </div>

    </div>

</div>





<div class="md-overlay"></div>

<div class="loader shadow radius-10 js-loader d-none" id="js-loader">

    <span class="icon icon-loader square-96"></span>

</div>



<script src="/site/templates/js/vendor/jquery-3.4.1.min.js?v=2"></script>

<script src="/site/templates/js/vendor/swiper.min.js"></script>

<script src="/site/templates/js/vendor/jquery.selectric.min.js"></script>

<script src="/site/templates/js/vendor/parsley.min.js"></script>

<script src="/site/templates/js/vendor/classie.js"></script>

<script src="/site/templates/js/vendor/jquery.fancybox.min.js"></script>

<script src="/site/templates/js/vendor/vanilla.filterizr.min.js"></script>

<script src="/site/templates/js/vendor/imagesloaded.pkgd.min.js"></script>

<script src="/site/templates/js/vendor/datepicker.min.js"></script>

<script src="/site/templates/js/validation.js"></script>





    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDhxv0wbEjcKEoCfWOd-TLHTRXLpLrDWzk"></script>

    <script src="/site/templates/js/map.js?v=1669294085"></script>





<script src="/site/templates/js/functions.js?v=1669294085"></script>

<script src="/site/templates/js/app.js?v=1669294085"></script>

</body>

</html>
 '''

soup = BeautifulSoup(markup, 'html.parser')


pagespace = soup.find(id="js-scroll-map")
first_h4 = str(pagespace.find('h4'))
length = len(str(pagespace.find('h4')))

locations = soup.find(class_="d-flex align-items-center justify-content-between cursor-p mb-4 js-slide-header events-none")
lat = locations.get('data-lat')
lng = locations.get('data-lng')
#print(f"lattitude: {lat}\nlongitude: {lng}")



#example on how to extract text in h4
#print(f"The length of below string is: {length}")
#print(pagespace.find('h4'))
#start_str = first_h4.index('>')
#end_str = first_h4.index('<',start_str+1)
#h4 = first_h4[start_str+1:end_str]
#print(h4)


#the loop to find all h4 elements where the store names reside and print to the txt file
#for h4 in pagespace:
#    with open("Araz_stores_names_h4.txt", "a", encoding="utf8") as f:
#        print(h4.find('h4'), file=f)

#the loop attempt to find the store names from h4 elements
#headers = []
#for h4 in pagespace:
#    headers.append(h4.find('h4'))

#Yuxaridkalari saxla

f = open('response(copy).json', encoding="utf8")

data = json.load(f)

jsonData = data[0]
for x in jsonData:
    keys = x.keys()
    print(keys)