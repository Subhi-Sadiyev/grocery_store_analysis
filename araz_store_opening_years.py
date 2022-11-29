import requests
from bs4 import BeautifulSoup
import json

response = requests.get('https://www.arazmarket.az/az/news/opening/')
html = response.text

#with open("araz_stores_years.txt", "w", encoding="utf8") as f:
 #   print(html, file=f)

markup = ''' 
<!DOCTYPE html>

<html lang="azərbaycanca">

<head prefix="og: http://ogp.me/ns#">

    <meta charset="UTF-8">

    <link rel='icon' href='/site/templates/img/favicon.png' type='image/x-icon'/>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title> | Araz Supermarket</title>

    <link rel="stylesheet" href="/site/templates/css/vendor/bootstrap-grid.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/swiper.min.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/selectric.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/jquery.background-video.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/jquery.fancybox.min.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/normalize.css">

    <link rel="stylesheet" href="/site/templates/css/vendor/datepicker.min.css?v=2">

    <link rel="stylesheet" href="/site/templates/css/style.css?v=1669739788">

    <link rel="stylesheet" href="/site/templates/fonts/stylesheet.css?v=1669739788">

    <link rel="stylesheet" href="/site/templates/css/vendor/fonts.css?v=1669739788">

    <link rel="stylesheet" href="/site/templates/css/additional.css?v=1669739788">

    <link rel="stylesheet" href="/site/templates/css/responsive.css?v=1669739788">





        <meta name="description" content="">

    <meta name="keywords" content="">

    <meta property="og:type" content="website"/>

    <meta property="og:title" content="Açılışlar"/>

    <meta property="og:image" content="https://www.arazmarket.az/site/templates/img/share-logo.jpg"/>

    <meta property="og:image:type" content="image/jpeg" />

    <meta property="og:image:width" content="200"/>

    <meta property="og:image:height" content="200"/>

    <meta property="og:url" content="https://www.arazmarket.az/az/news/opening/"/>

    <meta property="og:description" content=""/>

    <meta property="og:keywords" content=""/>



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
    <header class="bg-84bf41 bg-a bg-no-repeat bg-right-top">
        <section class="container">
            

<div class=" hover-node header-lg-animate z-100"
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
                            <a href="/az/stores/"                                class="fs-lg-18 underline-0 color-white border-white ">Mağazalar</a>
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
                        <option value="" data-url="/az/news/opening/" class="d-none">AZ</option><option value="uk" data-url="/en/news/opening/" >English</option><option value="ru" data-url="/ru/news/opening/" >Русский</option>                    </select>
            </div>
            <a href="/az/stores/"
               class="d-none d-lg-inline-flex square-40 square-lg-50 bg-white radius-50 mr-1 icon-location bg-center bg-no-repeat"></a>

            <span class="d-flex d-lg-none align-items-center pos-relative">
                <label for="js-selectric-lang-header"
                       class="d-flex square-40 square-lg-50 bg-white radius-50 hover-node border border-transparent cursor-p justify-content-center align-items-center pos-absolute right-0">
                    <span class="icon icon-2x icon-lang bg-center bg-no-repeat"></span>
                </label>

                <select class="selectric-tooltip label-fs-14 opacity-0" id="js-selectric-lang-header">
                    <option value="az" data-url="/az/news/opening/" class="d-none">AZ</option><option value="uk" data-url="/en/news/opening/" >English</option><option value="ru" data-url="/ru/news/opening/" >Русский</option>                </select>
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
            <div class="row h-380 h-lg-500 justify-content-center align-items-center text-center">
                <div class="col-lg-8 mt-5">
                    <h1 class="fs-lg-58 fw-700 color-white my-0">Xəbərlər</h1>
                    <p class="color-white fs-16 lh-24">“Araz” supermarketlər şəbəkəsi ilə bağlı ən yeni xəbərləri buradan izləyə bilərsiniz.</p>
                </div>
            </div>
        </section>
    </header>


    <section class="bg-f3fbff my-lg-5 py-4">
        <div class="container">
            <div class="row pt-70px pb-5">
                <div class="col-12 d-flex justify-content-center justify-content-lg-start">
                    <div class="d-inline-flex fs-14 fs-lg-16 lh-lg-24 color-70c21d card-border radius-6 overflowx-h">
                        <a href="/az/news/" class="px-3 px-lg-4 py-3 color-84bf41">
                            <span class="px-2">Hamısı</span>
                        </a>
                                                    <a href="/az/news/opening/"
                               class="px-3 px-lg-4 py-3 color-84bf41 left-b-ebebeb    shadow bg-84bf41 color-white">
                                <span class="px-2">Açılışlar</span>
                            </a>
                                                    <a href="/az/news/events/"
                               class="px-3 px-lg-4 py-3 color-84bf41 left-b-ebebeb  ">
                                <span class="px-2">Tədbirlər</span>
                            </a>
                                                    <a href="/az/news/projects/"
                               class="px-3 px-lg-4 py-3 color-84bf41 left-b-ebebeb  ">
                                <span class="px-2">Layihələr</span>
                            </a>
                                                    <a href="/az/news/ksm/"
                               class="px-3 px-lg-4 py-3 color-84bf41 left-b-ebebeb  ">
                                <span class="px-2">KSM</span>
                            </a>
                                            </div>
                </div>
            </div>


            <div class="row py-lg-5 mb-5 mt-3 font-inter">
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/ehmedlide-yeni-araz-supermarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4918/1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">25.11.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Əhmədlidə yeni &quot;Araz&quot; Supermarket! (25.11.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/n-rimanovda-yeni-araz-ekspress-05.10.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4906/nerimanov.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">05.11.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nərimanovda yeni &quot;Araz&quot; Ekspress! (05.10.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/neapolda-yeni-araz-minimarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4838/1-min.jpeg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">31.10.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Neapolda yeni &quot;Araz&quot; Minimarket! (31.10.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/i-nsaatcilarda-yeni-araz-minimarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4759/312340740_5442454442470131_1992804107769767655_n.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">22.10.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">İnşaatçılarda yeni &quot;Araz&quot; Minimarket! (22.10.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-xirdalan-superstore-da-19.10.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4700/312175211_5436330523082523_8595943845953255759_n.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">19.10.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">&quot;Pepco&quot; məhsulları “Araz” Xırdalan Superstore-da (19.10.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-space-superstore-da-03.10.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4513/pepco.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">03.10.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">&quot;Pepco&quot; məhsulları “Araz” Space Superstore-da (03.10.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bayilda-yeni-araz-supermarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4511/2-min.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">30.09.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Bayılda yeni &quot;Araz&quot; Supermarket! (30.09.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/xirdalanda-yeni-araz-supermarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4512/2-min_1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">30.09.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Xırdalanda yeni &quot;Araz&quot; Supermarket! (30.09.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/3-yeni-marketimiz-artiq-sizin-xidm-tinizd-dir/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4505/2-min.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">26.09.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">3 yeni marketimiz artıq sizin xidmətinizdədir!</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/zabratda-yeni-araz-minimarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4407/1-min.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">20.09.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Zabratda yeni &quot;Araz&quot; minimarket! (20.09.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-mehsullari-araz-resulzad-superstoreda-07.08.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4166/1_1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">07.08.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz&quot; Rəsulzadə Superstore&quot; da (07.08.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/kohn-gun-sli-q-s-b-sind-novb-ti-araz-market-06.08.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4167/img_8184.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">06.08.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Köhnə Günəşli qəsəbəsində növbəti &quot;Araz&quot; market! (06.08.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/xirdalanda-novb-ti-araz-market-03.08.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4133/2_1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">03.08.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Xırdalanda növbəti &quot;Araz&quot; market! (03.08.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-planet-supermarketd-28.07.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4127/1_1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">28.07.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz Planet Supermarket&quot;də (28.07.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-i-nqilab-superstoreda-21.07.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4111/a1.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">21.07.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz İnqilab Superstore&quot;da (21.07.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bakixanovda-yeni-araz-minimarket-20.07.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4093/bakixanov7.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">20.07.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Bakıxanovda növbəti &quot;Araz&quot; market! (20.07.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/samaxinkada-novb-ti-araz-market-20.07.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4094/samaxinka.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">20.07.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Şamaxinkada növbəti &quot;Araz&quot; market! (20.07.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-masazir-2-superstoreda-09.07.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4077/coverrrrrr.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">09.07.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları Araz Masazır-2 Superstoreda (09.07.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-masazir-3-superstoreda/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4046/cover.jpeg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">02.07.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz Masazır-3 Superstore&quot;da (02.07.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-bakixanov-superstoreda-25.06.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/4007/cover_h.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">25.06.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz Bakıxanov Superstore&quot;da! (25.06.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/m-c-mid-yeni-araz-minimarket-13.06.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3955/ecemi.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">13.06.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">M. Əcəmidə yeni &quot;Araz&quot; Minimarket! (13.06.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-9-mkr-2-superstoreda-09.06.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3953/ssssssss.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">09.06.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz 9 mkr 2 Superstore&quot;da! (09.06.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-hovsan-superstoreda-31.05.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3910/cover_h.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">31.05.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz Hövsan Superstore&quot;da! (31.05.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/tusid-novb-ti-araz-market-30.05.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3892/asdfg.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">30.05.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Tusidə növbəti &quot;Araz&quot; market! (30.05.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bil-c-rid-novb-ti-araz-market-26.05.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3886/a01.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">26.05.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Biləcəridə növbəti &quot;Araz&quot; market! (26.05.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bin-d-novb-ti-araz-market-23.05.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3868/a1.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">23.05.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Binədə növbəti &quot;Araz&quot; market! (23.05.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-novxani-superstoreda-21.05.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3867/cover_pepco.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">21.05.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz Novxanı Superstore&quot;da! (21.05.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/ataturkd-novb-ti-araz-market-29.04.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3763/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">29.04.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Atatürkdə növbəti &quot;Araz&quot; market! (29.04.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-20-yanvar-superstoreda-22.04.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3718/cover.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">22.04.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Pepco məhsulları &quot;Araz 20 yanvar Superstore&quot;da! (22.04.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-neftcil-r-superstoreda-14.04.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3704/cover.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">14.04.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“Pepco” məhsulları “Araz Neftçilər Superstore&quot;da! (14.04.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-sumqayit-superstoreda-07.04.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3675/cover.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">07.04.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“Pepco” məhsulları “Araz Sumqayıt Superstore&quot;da! (07.04.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/pepco-m-hsullari-araz-xirdalan-superstoreda-06.04.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3673/pepco_cover.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">06.04.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“Pepco” məhsulları “Araz Xırdalan Superstore&quot;da! (06.04.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/hm-dlid-novb-ti-araz-market-14.03.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3576/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">14.03.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Əhmədlidə növbəti &quot;Araz&quot; market! (14.03.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/zigda-novb-ti-araz-supermarket-22.01.2022/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3386/272206366_4660165924032324_3137613632613151030_n.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">22.01.2022</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Zığda növbəti &quot;Araz&quot; Supermarket! (22.01.2022)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/masazirda-yeni-araz-supermarket-24.12.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3276/269887220_4557591247623126_6275280817107593583_n.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">24.12.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Masazırda yeni &quot;Araz&quot; Supermarket! (24.12.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/sumqayitda-yeni-araz-supermarket-15.12.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3215/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">15.12.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Sumqayıtda yeni &quot;Araz&quot; Supermarket! ( 15.12.2021 )</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/ming-cevird-yeni-araz-minimarket-02.12.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3191/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">02.12.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Mingəçevirdə yeni &quot;Araz&quot; Minimarket! ( 02.12.2021 )</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/suv-landa-yeni-araz-supermarket-26.11.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3181/261629656_4452151728167079_3754496880064169373_n.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">29.11.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Şüvəlanda yeni Araz Supermarket ( 26.11.2021 )</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/masazirda-yeni-araz-minimarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3131/ueddqud3de234re34.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">30.10.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Masazırda yeni &quot;Araz&quot; Minimarket! ( 30.10.2021 )</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bil-c-rid-yeni-araz-minimarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3127/a1_2.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">29.10.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Biləcəridə yeni &quot;Araz&quot; Minimarket!</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/h-zi-aslanovda-yeni-araz-ekspress-28.10.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3126/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">28.10.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Həzi Aslanovda yeni &quot;Araz&quot; Ekspress! ( 28.10.2021 )</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/susada-yeni-araz-supermarket-04.10.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/3022/1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">04.10.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Şuşada yeni &quot;Araz&quot; Supermarket! ( 04.10.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/yevlaxda-yeni-araz-supermarket/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2954/1.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">21.09.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Yevlaxda yeni &quot;Araz&quot; Supermarket!</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/sumqayitda-yeni-araz-supermarket-31.07.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2864/4111.png" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">31.07.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Sumqayıtda yeni &quot;Araz&quot; Supermarket! (31.07.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/n-rimanovda-yeni-araz-supermarket-29.07.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2863/efuefu.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">29.07.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nərimanovda yeni &quot;Araz&quot; Supermarket! (29.07.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/hm-dlid-yeni-araz-minimarket-24.06.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2768/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">24.06.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Əhmədlidə yeni &quot;Araz&quot; Minimarket! (24.06.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/s-kid-yeni-araz-supermarket-15.06.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2738/h1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">15.06.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Şəkidə yeni &quot;Araz&quot; Supermarket! (15.06.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/n-rimanov-rayonunda-yeni-araz-minimarket-11.06.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2732/a1_1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">11.06.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nərimanov rayonunda yeni &quot;Araz&quot; Minimarket! (11.06.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/mehdiabadda-yeni-araz-supermarket-09.06.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2721/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">09.06.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Mehdiabadda yeni &quot;Araz&quot; Supermarket! (09.06.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/ramanada-yeni-araz-minimarket-07.06.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2718/a0.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">07.06.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Ramanada yeni &quot;Araz&quot; Minimarket! (07.06.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/yasamalda-yeni-araz-minimarket-30.05.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2691/11111.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">30.05.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Yasamalda yeni &quot;Araz&quot; Minimarket! (30.05.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/yasamalda-yeni-araz-supermarket-f-aliyy-t-basladi-25.05.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2682/d1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">25.05.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Yasamalda yeni &quot;Araz Supermarket&quot; fəaliyyətə başladı (25.05.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/abseronda-yeni-araz-superstore-f-aliyy-t-basladi-07.05.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2642/sayt.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">07.05.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Abşeronda yeni &quot;Araz Superstore&quot; fəaliyyətə başladı (07.05.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/g-nc-d-yeni-araz-supermarket-f-aliyy-t-basladi-18.03.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2332/a1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">18.03.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Gəncədə yeni “Araz Supermarket” fəaliyyətə başladı ( 18.03.2021 )</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bin-q-did-yeni-araz-superstore-f-aliyy-t-basladi-16.03.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2319/acilis_sayt.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">16.03.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Binəqədidə yeni “Araz Superstore” fəaliyyətə başladı ( 16.03.2021 )</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/hovsan-q-s-b-sind-yeni-araz-supermarket-f-aliyy-t-basladi-27.02.2021/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2272/su.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">27.02.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Hövsan qəsəbəsində yeni “Araz Supermarket” fəaliyyətə başladı (27.02.2021)</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/badamdar-q-s-b-sind-yeni-araz-minimarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2246/acilis_yeniun-1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">23.02.2021</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Badamdar qəsəbəsində yeni “Araz” minimarket fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/n-rimanov-rayonunda-yeni-araz-minimarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2083/1-1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">30.12.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nərimanov rayonunda yeni “Araz minimarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/hovsan-q-s-b-sind-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2071/hovsan.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">24.12.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Hövsan qəsəbəsində yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bakixanov-q-s-b-sind-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2072/bk.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">24.12.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Bakıxanov qəsəbəsində yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/m-h-mm-di-k-ndind-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2073/mh.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">24.12.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Məhəmmədi kəndində yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/n-rimanov-rayonunda-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/2074/nb.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">24.12.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nərimanov rayonunda yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-nizami-rayonunda-novb-ti-filialini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1923/c2bfcb50-f55f-415a-8c87-524eb1278f29.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">04.12.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“Araz” supermarketlər şəbəkəsi Nizami rayonunda növbəti filialını açdı.</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/nardaran-q-s-b-sind-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1917/yeni.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">02.12.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nardaran qəsəbəsində yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/n-simi-rayonunda-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1774/yeni.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">10.11.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nəsimi rayonunda yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/x-tai-rayonunda-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1731/img_9082.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">25.10.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Xətai rayonunda yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bin-d-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1668/yeni.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">25.09.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Binədə yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/gun-slid-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1667/yeni.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">25.09.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Günəşlidə yeni “Araz Supermarket” fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/nizami-rayonunda-yeni-araz-supermarket-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1627/fff.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">15.09.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Nizami rayonunda yeni &quot;Araz Supermarket&quot; fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bakinin-n-rimanov-rayonunda-yeni-araz-market-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1591/q1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">11.08.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Bakının Nərimanov rayonunda yeni “Araz” market fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/x-tai-rayonunda-yeni-araz-market-acildi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1590/t1.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">31.07.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Xətai rayonunda yeni “Araz” market açıldı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bakinin-n-rimanov-rayonunda-4-cu-araz-market-f-aliyy-t-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1589/n4.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">06.07.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Bakının Nərimanov rayonunda 4-cü “Araz” market fəaliyyətə başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-sumqayitda-yeni-minimarket-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1271/news1-pic.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">19.05.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">&quot;Araz&quot; supermarketlər şəbəkəsi Sumqayıtda yeni minimarket açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-isci-q-bulu-elan-edir/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1418/50.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">03.04.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“Araz” supermarketlər şəbəkəsi işçi qəbulu elan edir</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-saray-2-filialini-must-ril-rin-ixtiyarina-verdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1419/32.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">13.03.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">&quot;Araz&quot; supermarketlər şəbəkəsi Saray 2 filialını müştərilərin ixtiyarına verdi</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-yasamal-rayonunda-novb-ti-filialini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1427/34.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">31.01.2020</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">&quot;Araz&quot; supermarketlər şəbəkəsi Yasamal rayonunda növbəti filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-badamdar-q-s-b-sind-novb-ti-filialini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1429/46.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">26.12.2019</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">&quot;Araz&quot; supermarketlər şəbəkəsi Badamdar qəsəbəsində növbəti filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-n-simi-rayonunda-novb-ti-filialini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1430/35.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">21.11.2019</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“Araz” supermarketlər şəbəkəsi Nəsimi rayonunda növbəti filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-kurd-xani-q-s-b-si-nd-novb-ti-fi-li-alini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1433/40.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">25.10.2019</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“ARAZ” Supermarketlər şəbəkəsi Kürdəxanı qəsəbəsində növbəti filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-novb-ti-fi-li-alini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1435/41.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">13.09.2019</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarketlər şəbəkəsi növbəti filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-tender-elan-edi-r/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1436/38.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">06.09.2019</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarketlər şəbəkəsi tender elan edir</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-yeni-suraxani-q-s-b-si-nd-novb-ti-fi-li-alini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1423/32.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">31.05.2019</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“ARAZ” supermarketlər şəbəkəsi Yeni Suraxanı qəsəbəsində növbəti filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-novb-ti-ekspress-fi-li-alini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1424/31.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">22.05.2019</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“ARAZ” supermarketlər şəbəkəsi növbəti ekspress filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-zaqatalada-yeni-fi-li-alini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1439/19.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">15.12.2017</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarketlər şəbəkəsi Zaqatalada yeni filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-n-boyuk-fi-li-alini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1440/18.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">15.11.2017</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarketlər şəbəkəsi ən böyük filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarket-v-favori-t-market-s-b-k-l-ri-birl-sir/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1441/17.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">29.09.2017</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">“ARAZ Supermarket” və “FAVORİT Market” şəbəkələri birləşir</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarket-tari-xi-nd-bi-r-i-lk/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1443/15.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">04.07.2017</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarket tarixində bir ilk</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-nd-n-novb-ti-yeni-li-k/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1444/14.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">06.04.2017</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarketlər şəbəkəsindən növbəti yenilik</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-i-lk-ekspress-fi-li-alini-acdi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1446/12.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">16.02.2017</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarketlər şəbəkəsi ilk ekspress filialını açdı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/araz-supermarketl-r-s-b-k-si-nd-n-t-l-b-l-r-d-st-k/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1448/10.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">14.12.2016</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">ARAZ Supermarketlər şəbəkəsindən tələbələrə dəstək</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/moht-s-m-100-gun-yeni-d-n-basladi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1449/7.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">01.10.2016</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Möhtəşəm 100 gün yenidən başladı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/bakida-daha-bir-araz-market-acildi/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1450/5.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">14.06.2016</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">Bakıda daha bir Araz Market açıldı</p>
                                </div>
                            </div>
                        </a>
                    </div>
                                    <div class="col-lg-4 pt-70px d-flex mt-2 mb-4">
                        <a href="/az/news/opening/arazdan-sarayda-f-rqli-market/" class="radius-10 card bg-white card-border hover-node">
                            <figure>
                                                                    <img src="/site/assets/files/1451/4.jpg" alt=""
                                         class="w-100 obj-cover blog-card-img-h radius-t10 d-block">
                                                            </figure>
                            <div class="p-4 pb-5 radius-b10">
                                <div class="p-2">
                                    <span class="color-70c21d lh-lg-16 fw-700 mt-2">14.06.2016</span>
                                    <p class="fw-500 fs-18 lh-32 color-black m-0 mt-3">&quot;Araz&quot;dan Sarayda fərqli market</p>
                                </div>
                            </div>
                        </a>
                    </div>
                            </div>
        </div>
    </section>


    <div class="bg-f3fbff">
        <footer>

    <section class="container">

        <div class="row py-4 align-items-center bottom-b-ebebeb top-b-ebebeb border-lg-top-0">

            <div class="col-lg-8 d-lg-flex pos-relative">

                <a href="/" class="d-none d-lg-inline-flex pr-4 mr-3">

                    <span class="icon logo2 logo-size"></span>

                </a>



                <div class="d-flex d-lg-none justify-content-between">

                                            <a href="https://apps.apple.com/az/app/araz/id1478404022" target="_blank"

                           class="d-inline-flex p-3 border-ebebeb border color-b5b5b5 radius-6  hover-node hover-darkest">

                            <span class="icon icon-app-store icon-2x"

                                  style="background-image:url(/site/assets/files/1312/app-store.svg)"></span>

                            <div class="ml-2">

                                <span class="d-block fw-500 fs-12">Download on</span>

                                <span class="d-block fw-500 fs-18">App Store</span>

                            </div>

                        </a>

                                            <a href="https://play.google.com/store/apps/details?id=com.araz&hl=ru" target="_blank"

                           class="d-inline-flex p-3 border-ebebeb border color-b5b5b5 radius-6 ml-xs-1 ml-4 hover-node hover-darkest">

                            <span class="icon icon-app-store icon-2x"

                                  style="background-image:url(/site/assets/files/1313/google-play.svg)"></span>

                            <div class="ml-2">

                                <span class="d-block fw-500 fs-12">Get it on</span>

                                <span class="d-block fw-500 fs-18">Google Play</span>

                            </div>

                        </a>

                                    </div>



                <div class="d-lg-inline-flex fs-lg-18 fw-700 align-items-center flex-wrap hover-link-underline">

                                            <a href="/az/about-us/"

                           class="color-e7792b underline-0 d-inline-flex mr-4 pr-2 pr-lg-0 pt-4 pt-lg-0">Haqqımızda</a>

                                            <a href="/az/campaigns/"

                           class="color-e7792b underline-0 d-inline-flex mr-4 pr-2 pr-lg-0 pt-4 pt-lg-0">Kampaniyalar</a>

                                            <a href="/az/stores/"

                           class="color-e7792b underline-0 d-inline-flex mr-4 pr-2 pr-lg-0 pt-4 pt-lg-0">Mağazalar</a>

                                            <a href="/az/career/"

                           class="color-e7792b underline-0 d-inline-flex mr-4 pr-2 pr-lg-0 pt-4 pt-lg-0">Karyera</a>

                                            <a href="/az/app/"

                           class="color-e7792b underline-0 d-inline-flex mr-4 pr-2 pr-lg-0 pt-4 pt-lg-0">Siz harada, &quot;Araz&quot; mobil tətbiqi orada</a>

                                    </div>

            </div>



            <div class="col-lg-4 d-none d-lg-flex justify-content-end">

                                    <a href="https://apps.apple.com/az/app/araz/id1478404022" target="_blank"

                       class="d-inline-flex p-3 border-ebebeb border color-b5b5b5 radius-6  hover-node hover-darkest">

                            <span class="icon icon-app-store icon-2x"

                                  style="background-image:url(/site/assets/files/1312/app-store.svg)"></span>

                        <div class="ml-2">

                            <span class="d-block fw-500 fs-12">Download on</span>

                            <span class="d-block fw-500 fs-18">App Store</span>

                        </div>

                    </a>

                                    <a href="https://play.google.com/store/apps/details?id=com.araz&hl=ru" target="_blank"

                       class="d-inline-flex p-3 border-ebebeb border color-b5b5b5 radius-6 ml-4 hover-node hover-darkest">

                            <span class="icon icon-app-store icon-2x"

                                  style="background-image:url(/site/assets/files/1313/google-play.svg)"></span>

                        <div class="ml-2">

                            <span class="d-block fw-500 fs-12">Get it on</span>

                            <span class="d-block fw-500 fs-18">Google Play</span>

                        </div>

                    </a>

                            </div>

        </div>



        <div class="row py-4 align-items-center bottom-b-ebebeb top-b-ebebeb justify-content-between" style="display: none;">

            <div class="col-lg-4">

                <p class="color-7c869e fs-lg-24 fw-500">Yeniliklərdən xəbərdar olmaq üçün abunə ol</p>

            </div>

            <div class="col-lg-6">

                <div class="subscribe_form">

                    <div class="subscribe_tabs">

                        <label>

                            <input type="radio" name="name_1" checked>

                            <span>Elektron-ünvan</span>

                        </label>

                        <label>

                            <input type="radio" name="name_1">

                            <span>Mobil nömrə</span>

                        </label>

                    </div>

                    <div class="input_send">

                        <div class="input">

                            <input type="text" placeholder="simple@gmail.com">

                        </div>

                        <div class="button">

                            <a href="javascript:void(0);">Göndər</a>

                        </div>

                    </div>

                </div>

            </div>

        </div>



        <div class="row pt-3 pb-4 align-items-center">

            <div class="col-12">

                <ul class="d-flex list-reset fs-lg-14 align-items-center pt-2 pb-2 pb-lg-0 mb-4 mb-lg-3 hover-link-underline-none">

                                            <li class="pr-4">

                            <a href="/az/news/"

                               class="color-7c869e underline">Xəbərlər</a>

                        </li>

                                            <li class="pr-4">

                            <a href="/az/blog/"

                               class="color-7c869e underline">Bloq</a>

                        </li>

                                            <li class="pr-4">

                            <a href="/az/gallery/"

                               class="color-7c869e underline">Qalereya</a>

                        </li>

                                    </ul>

            </div>

            

            <div class="col-lg-8 d-lg-flex align-items-center align-items-center justify-content-lg-between">

                <p class="m-0 pr-4 color-7c869e pt-2 d-none d-lg-inline-flex fs-14">BÜTÜN HÜQUQLAR QORUNUR © ARAZ SUPERMARKET 2022</p>



                <a href="https://jis.az" target="_blank" class="d-flex align-items-center fs-13 color-black mb-4 mb-lg-0">

                    <span class="opacity-5">Site by</span>

                    <span class="icon square-20 icon-jis mx-2"></span>

                    <strong class="opacity-5">Jeykhun Imanov Studio</strong>

                </a>

            </div>



            <div class="col-lg-4 d-flex px-lg-0 justify-content-lg-end align-items-center right_footer">

                                    <a href="https://www.facebook.com/arazsupermarket/" target="_blank"

                       class="radius-50 d-inline-flex justify-content-center align-items-center bg-f3f1f7 square-40 mr-3 hover-node hover-darker">

                        <span class="icon square-16"

                              style="background-image:url(/site/assets/files/1314/fb.svg)"></span>

                    </a>

                                    <a href="https://www.instagram.com/arazsupermarket/" target="_blank"

                       class="radius-50 d-inline-flex justify-content-center align-items-center bg-f3f1f7 square-40 mr-3 hover-node hover-darker">

                        <span class="icon square-16"

                              style="background-image:url(/site/assets/files/1315/instagram.svg)"></span>

                    </a>

                                    <a href="https://www.tiktok.com/@arazsupermarket?source=h5_m" target="_blank"

                       class="radius-50 d-inline-flex justify-content-center align-items-center bg-f3f1f7 square-40 mr-3 hover-node hover-darker">

                        <span class="icon square-16"

                              style="background-image:url(/site/assets/files/1337/tiktok-icon.svg)"></span>

                    </a>

                                    <a href="https://www.linkedin.com/company/araz-supermarket-mmc/" target="_blank"

                       class="radius-50 d-inline-flex justify-content-center align-items-center bg-f3f1f7 square-40 mr-3 hover-node hover-darker">

                        <span class="icon square-16"

                              style="background-image:url(/site/assets/files/1335/linked-in.svg)"></span>

                    </a>

                                    <a href="https://www.youtube.com/channel/UCV-zOsEjYN7eucr34wPOHRg?view_as=subscriber" target="_blank"

                       class="radius-50 d-inline-flex justify-content-center align-items-center bg-f3f1f7 square-40 mr-3 hover-node hover-darker">

                        <span class="icon square-16"

                              style="background-image:url(/site/assets/files/1336/youtube.svg)"></span>

                    </a>

                                    <a href="https://t.me/arazsupermarket" target="_blank"

                       class="radius-50 d-inline-flex justify-content-center align-items-center bg-f3f1f7 square-40 mr-3 hover-node hover-darker">

                        <span class="icon square-16"

                              style="background-image:url(/site/assets/files/1831/tq.svg)"></span>

                    </a>

                

                <span>

                    <select class="selectric-tooltip label-fs-14" id="js-selectric-lang-footer2">

                        <option value="" data-url="/az/news/opening/" class="d-none">AZ</option><option value="uk" data-url="/en/news/opening/" >English</option><option value="ru" data-url="/ru/news/opening/" >Русский</option>                    </select>

                </span>

            </div>



            <p class="fs-14 col-12 pr-4 color-7c869e pt-2 d-lg-none">BÜTÜN HÜQUQLAR QORUNUR © ARAZ SUPERMARKET 2022</p>

        </div>

    </section>

</footer>





<div class="modal_darkness"></div>





<div class="video_modal">

  <div class="video">

    <iframe width="800" height="450" src="https://www.youtube.com/embed/p7FPwt2n3AU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

  </div>

  <a href="javascript:void(0)" class="close"></a>

</div>    </div>

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



<div class="md-modal md-effect-14 " id="modal-campaign" >

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









<script src="/site/templates/js/functions.js?v=1669739789"></script>

<script src="/site/templates/js/app.js?v=1669739789"></script>

</body>

</html>

'''

soup = BeautifulSoup(markup, 'html.parser')


pagespace = soup.find(class_="row py-lg-5 mb-5 mt-3 font-inter")

#entire div with class row
#with open("araz_stores_years.txt", "w", encoding="utf-8", ) as f:
 #   print(pagespace, file=f)



paragraphs = []
paragraphs_str = str(paragraphs)
for p in pagespace:
    paragraphs.append(p.find("p"))

new_paragraphs = []
for string in paragraphs:
    new_paragraphs.append(str(string))



new_paragraphs_str = str.join("",new_paragraphs)

print(new_paragraphs_str)

with open("araz_stores_years.txt", "w", encoding="utf-8" ) as f:
    f.write(new_paragraphs_str)