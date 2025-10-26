<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="keywords" content="">
	<meta name="author" content="">
	<meta name="robots" content="">
	<meta name="description" content="Industry - Factory & Industrial HTML Template">
	<meta property="og:title" content="Industry - Factory & Industrial HTML Template">
	<meta property="og:description" content="Industry - Factory & Industrial HTML Template">
	<meta property="og:image" content="https://industry.dexignzone.com/xhtml/social-image.webp">
	<meta name="format-detection" content="telephone=no">
	
	<!-- FAVICONS ICON -->
	<link rel="icon" href="images/favicon.ico" type="image/x-icon">
	<link rel="shortcut icon" type="image/x-icon" href="images/favicon.webp">
	
	<!-- PAGE TITLE HERE -->
	<title>弗劳恩生物</title>
	
	<!-- MOBILE SPECIFIC -->
	<meta name="viewport" content="width=device-width, initial-scale=1">
	
	<!--[if lt IE 9]>
	<script src="js/html5shiv.min.js"></script>
	<script src="js/respond.min.js"></script>
	<![endif]-->
	
		<!-- STYLESHEETS -->
	<link rel="stylesheet" type="text/css" href="css/plugins.css">
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<link class="skin" rel="stylesheet" type="text/css" href="css/skin/skin-4.css">
	<link rel="stylesheet" type="text/css" href="css/templete.css">
	<!-- Google Font -->	
	<style>
		.big-number {
			font-size: 168px;
			font-weight: bold;
			color: #ccc; /* 淡灰色 */
			text-align: center;
			margin-left: 40px;
			opacity: 0;
			animation: fadeInUp 1s ease-out forwards;
		}

	@import url('https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i|Playfair+Display:400,400i,700,700i,900,900i|Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i|Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i|Roboto+Condensed:300,300i,400,400i,700,700i|Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&display=swap');
	</style>
</head>
<body id="bg">
<div class="page-wraper">
<div id="loading-area"></div>

    <!-- header -->
    <?php include 'header.php'; ?>
    <!-- header END -->
    <!-- Content -->
    <div class="page-content bg-white">

		<div class="dlab-bnr-inr bg-pt" style="background-image:url(images/banner/banner-5.webp);">
            <div class="container">
                <div class="dlab-bnr-inr-entry">
                    <h1 class="text-white" data-i18n="banner.title">研发与服务</h1>
					<!-- Breadcrumb row -->
					<div class="breadcrumb-row">
						<ul class="list-inline">
							<li><a href="index" data-i18n="banner.home">首页</a></li>
							<li data-i18n="banner.current">研发与服务</li>
						</ul>
					</div>
					<!-- Breadcrumb row END -->
                </div>
            </div>
        </div>

		
    </div>
    <!-- Content END-->
	<!-- Footer -->
    <?php include 'footer.php'; ?>
    <!-- Footer End -->
    <!-- scroll top button -->
    <button class="scroltop fas fa-chevron-up" ></button>
</div>
<!-- JAVASCRIPT FILES ========================================= -->
<script src="js/jquery.min.js"></script><!-- JQUERY.MIN JS -->
<script src="plugins/wow/wow.js"></script><!-- WOW JS -->

<script src="js/jquery.lazy.min.js"></script>

<script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><!-- BOOTSTRAP.MIN JS -->
<script src="plugins/bootstrap-select/bootstrap-select.min.js"></script><!-- FORM JS -->
<script src="plugins/bootstrap-touchspin/jquery.bootstrap-touchspin.js"></script><!-- FORM JS -->
<script src="plugins/magnific-popup/magnific-popup.js"></script><!-- MAGNIFIC POPUP JS -->
<script src="plugins/counter/waypoints-min.js"></script><!-- WAYPOINTS JS -->
<script src="plugins/counter/counterup.min.js"></script><!-- COUNTERUP JS -->
<script src="plugins/imagesloaded/imagesloaded.js"></script><!-- IMAGESLOADED -->
<script src="plugins/masonry/masonry-3.1.4.js"></script><!-- MASONRY -->
<script src="plugins/masonry/masonry.filter.js"></script><!-- MASONRY -->
<script src="plugins/owl-carousel/owl.carousel.js"></script><!-- OWL SLIDER -->
<script src="plugins/lightgallery/js/lightgallery-all.min.js"></script><!-- Lightgallery -->
<script src="plugins/scroll/scrollbar.min.js"></script><!-- scroll -->
<script src="js/custom.js"></script><!-- CUSTOM FUCTIONS  -->
<script src="js/dz.carousel.min.js"></script><!-- SORTCODE FUCTIONS  -->
<script src="plugins/countdown/jquery.countdown.js"></script><!-- COUNTDOWN FUCTIONS  -->
<script src="js/dz.ajax.js"></script><!-- CONTACT JS  -->

<script>
(function () {
  // 统一获取/设置语言
  function getLang() {
    var url = new URL(window.location.href);
    var urlLang = url.searchParams.get('lang');
    var savedLang = localStorage.getItem('lang');
    var htmlLang  = document.documentElement.getAttribute('lang');
    return (urlLang || savedLang || htmlLang || 'zh').toLowerCase();
  }
  function setLangAndReload(next) {
    if (!next) return;
    localStorage.setItem('lang', next);
    var u = new URL(window.location.href);
    u.searchParams.set('lang', next);
    window.location.href = u.toString();
  }

  // 初始化语言到 <html lang>
  var lang = getLang();
  if (document.documentElement.getAttribute('lang') !== lang) {
    document.documentElement.setAttribute('lang', lang);
  }
  localStorage.setItem('lang', lang);

  // ✅ 事件委托：捕获任意位置/任何时机出现的 a[data-lang]
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-lang]');
    if (!a) return;
    e.preventDefault();
    var picked = a.getAttribute('data-lang');
    if (!picked || picked === lang) return;
    setLangAndReload(picked);
  });

  // 可选：更新下拉按钮当前语言文案（如果存在 #langToggle）
  document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.getElementById('langToggle');
    if (toggle && toggle.firstChild) {
      toggle.firstChild.nodeValue = (lang === 'en' ? 'English' : '中文') + ' ';
    }
  });

  // 暴露给 i18n loader 使用
  window.__getLang = getLang;
})();
</script>


<script>
  // 取值工具：a.b.c
  function deepGet(obj, path) {
    return path.split('.').reduce((o, k) => (o && o[k] !== undefined ? o[k] : null), obj);
  }

  // 写文本但保留 <i> 等子节点：优先改第一个文本节点
  function setTextPreserveIcons(el, text) {
    const node = Array.from(el.childNodes).find(n => n.nodeType === Node.TEXT_NODE);
    if (node) node.nodeValue = text + ' ';
    else el.insertBefore(document.createTextNode(text + ' '), el.firstChild);
  }

  async function loadI18n(lang) {
    const pagePath   = `content/contact.${lang}.json`;
    const headerPath = `content/header.${lang}.json`;
    const footerPath = `content/footer.${lang}.json`;

    async function fetchOrZh(path, zhPath) {
      try {
        const r = await fetch(path, { cache: 'no-cache' });
        if (!r.ok) throw 0;
        return await r.json();
      } catch (_) {
        const r2 = await fetch(zhPath, { cache: 'no-cache' });
        return r2.ok ? await r2.json() : {};
      }
    }

    // 并行拉两份，各自兜底到 zh
    const [pageDict, headerDict, footerDict] = await Promise.all([
      fetchOrZh(pagePath,   'content/contact.zh.json'),
      fetchOrZh(headerPath, 'content/header.zh.json'),
      fetchOrZh(footerPath, 'content/footer.zh.json')
    ]);

    // 遍历填充
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const fullKey = el.getAttribute('data-i18n');
      const attr    = el.getAttribute('data-i18n-attr');

      let val = null;
      if (fullKey.startsWith('header.')) {
        val = deepGet(headerDict, fullKey.slice('header.'.length));
      } else if (fullKey.startsWith('footer.')) {
        val = deepGet(footerDict, fullKey.slice('footer.'.length));
      } else {
        val = deepGet(pageDict, fullKey);
      }
      if (val == null) return;

      if (attr) {
        el.setAttribute(attr, val);
      } else if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.setAttribute('placeholder', val);
      } else if (el.tagName === 'META') {
        el.setAttribute('content', val);
      } else {
        setTextPreserveIcons(el, val);
      }
    });

	// ✅ 正确处理 data-i18n-html（支持 header.* 命名空间）
	document.querySelectorAll('[data-i18n-html]').forEach(el => {
	const fullKey = el.getAttribute('data-i18n-html');
	let val = null;
	if (fullKey.startsWith('header.')) {
		val = deepGet(headerDict, fullKey.slice('header.'.length));
	} else {
		val = deepGet(pageDict, fullKey);
	}
	if (val != null) el.innerHTML = val;
	});

    // 同步 <title>
    const titleEl = document.querySelector('title[data-i18n="meta.title"]');
    if (titleEl) document.title = titleEl.textContent || document.title;

    // 更新语言下拉按钮显示（若有）
    const toggle = document.getElementById('langToggle');
    if (toggle) {
      const label = deepGet(headerDict, 'lang.toggle');
      if (label) setTextPreserveIcons(toggle, label);
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    const lang = (window.__getLang ? window.__getLang() : (document.documentElement.getAttribute('lang') || 'zh')).toLowerCase();
    loadI18n(lang);
    if (window.$ && $.fn.lazy) { $('.lazy').Lazy(); }
  });
</script>
<!-- 
<script>
jQuery(document).ready(function() {
	'use strict';
	// jQuery("#welcome").show();
	// dz_rev_slider_1();	
	$('.lazy').Lazy();
});	/*ready*/
</script> -->



</body>
</html>
