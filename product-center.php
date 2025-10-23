<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="keywords" content="">
  <meta name="author" content="">
  <meta name="robots" content="">
  <title data-i18n="meta.title"></title>
  <meta name="description" content="" data-i18n="meta.description">
  <meta name="format-detection" content="telephone=no">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="icon" href="images/favicon.ico" type="image/x-icon">
  <link rel="shortcut icon" type="image/x-icon" href="images/favicon.png">

  <!-- STYLESHEETS -->
  <link rel="stylesheet" href="css/plugins.css">
  <link rel="stylesheet" href="css/style.css">
  <link class="skin" rel="stylesheet" href="css/skin/skin-4.css">
  <link rel="stylesheet" href="css/templete.css">

  <style>
    h5 a:hover, p a:hover, .widget ul li a:hover { color:#FF8500; }
    .prod-row { margin-bottom: 20px; }
    .prod-thumb {
      margin-right: 30px; width: 200px; height: 200px;
      border: 2px solid #ddd; display:flex; justify-content:center; align-items:center; overflow:hidden;
    }
  </style>
</head>
<body id="bg">
<div class="page-wraper">
<div id="loading-area"></div>

  <!-- header -->
  <?php include 'header.php'; ?>
  <!-- header END -->

  <!-- Banner -->
  <div class="dlab-bnr-inr overlay-black-middle bg-pt" style="background-image:url(images/banner/banner-1.webp);">
    <div class="container">
      <div class="dlab-bnr-inr-entry">
        <h1 class="text-white" data-i18n="banner.title"></h1>
        <div class="breadcrumb-row">
          <ul class="list-inline">
            <li><a href="index" data-i18n="breadcrumb.home"></a></li>
            <li data-i18n="breadcrumb.current"></li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Content -->
  <div class="page-content bg-white">
    <div class="content-block">
      <div class="section-full content-inner">
        <div class="container">
          <div class="row">

            <!-- Sidebar -->
            <div class="col-lg-3 col-md-4 m-b30">
              <aside class="side-bar shop-categories sticky-top">
                <div class="widget recent-posts-entry">
                  <div class="dlab-accordion advanced-search toggle" id="accordion1">

                    <div class="panel">
                      <div class="">
                        <h4 class="acod-title">
                          <a href="#categories" style="color:#FF8500;" data-i18n="sidebar.title"></a>
                        </h4>
                      </div>
                    </div>

                    <div class="panel" style="margin-top:10px;">
                      <div class="acod-head">
                        <h5 class="acod-title">
                          <a data-bs-toggle="collapse" href="#Fetal-Bovine-Serum" data-i18n="sidebar.groups.fbs"></a>
                        </h5>
                      </div>
                      <div id="Fetal-Bovine-Serum" class="acod-body collapse">
                        <div class="acod-content">
                          <div class="widget widget_services">
                            <ul class="list-star red">
                              <li><a href="products/Front-Biomed-Premium-Imported-FBS" data-i18n="sidebar.items.fbs_imported"></a></li>
                              <li><a href="products/Front-Biomed-Superior-Grade-Fetal-Bovine-Serum" data-i18n="sidebar.items.fbs_domestic"></a></li>
                              <li><a href="products/Front-Biomed-Exceptional" data-i18n="sidebar.items.fbs_exceptional"></a></li>
                              <li><a href="products/Front-Biomed-Premium-FBS" data-i18n="sidebar.items.fbs_premium"></a></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div class="panel" style="margin-top:10px;">
                      <div class="acod-head">
                        <h5 class="acod-title">
                          <a data-bs-toggle="collapse" href="#Bovine-Serum" data-i18n="sidebar.groups.bovine"></a>
                        </h5>
                      </div>
                      <div id="Bovine-Serum" class="acod-body collapse">
                        <div class="acod-content">
                          <div class="widget widget_services">
                            <ul class="list-star red">
                              <li><a href="products/Newborn-Calf-Serum" data-i18n="sidebar.items.nbcs"></a></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div class="panel" style="margin-top:10px;">
                      <div class="acod-head">
                        <h5 class="acod-title">
                          <a data-bs-toggle="collapse" href="#other-serums" data-i18n="sidebar.groups.other_serum"></a>
                        </h5>
                      </div>
                      <div id="other-serums" class="acod-body collapse">
                        <div class="acod-content">
                          <div class="widget widget_services">
                            <ul class="list-star red">
                              <li><a href="products/Pig-Serum" data-i18n="sidebar.items.pig"></a></li>
                              <li><a href="products/Horse-Serum" data-i18n="sidebar.items.horse"></a></li>
                              <li><a href="products/Goat-Serum" data-i18n="sidebar.items.goat"></a></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div class="panel" style="margin-top:10px;">
                      <div class="acod-head">
                        <h5 class="acod-title">
                          <a data-bs-toggle="collapse" href="#Cell-Culture-Medium" data-i18n="sidebar.groups.medium"></a>
                        </h5>
                      </div>
                      <div id="Cell-Culture-Medium" class="acod-body collapse">
                        <div class="acod-content">
                          <div class="widget widget_services">
                            <ul class="list-star red">
                              <li><a href="products/DMEM-Cell-Culture-Medium" data-i18n="sidebar.items.dmem"></a></li>
                              <li><a href="products/MEM-Cell-Culture-Medium" data-i18n="sidebar.items.mem"></a></li>
                              <li><a href="products/RPMI-Cell-Culture-Medium" data-i18n="sidebar.items.rpmi"></a></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div class="panel" style="margin-top:10px;">
                      <div class="acod-head">
                        <h5 class="acod-title">
                          <a data-bs-toggle="collapse" href="#other" data-i18n="sidebar.groups.others"></a>
                        </h5>
                      </div>
                      <div id="other" class="acod-body collapse">
                        <div class="acod-content">
                          <div class="widget widget_services">
                            <ul class="list-star red">
                              <li><a href="products/Trypsin-0.05" data-i18n="sidebar.items.trypsin005"></a></li>
                              <li><a href="products/Trypsin-0.25" data-i18n="sidebar.items.trypsin025"></a></li>
                              <li><a href="products/Double-Antibiotic" data-i18n="sidebar.items.antibiotic"></a></li>
                              <li><a href="products/Frozen-Cell-Suspension" data-i18n="sidebar.items.frozen"></a></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              </aside>
            </div>
            <!-- Sidebar END -->

            <!-- Main list -->
            <div class="col-xl-9 col-lg-8 col-md-7 m-b30">
              <div class="row">

                <!-- 产品1：进口特级 FBS -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/products/new-product1-side.webp"
                              alt="" data-i18n="products.items.0.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Front-Biomed-Premium-Imported-FBS" data-i18n="products.items.0.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
								<div style="flex:1;margin-left:20px;font-size:14px;line-height:1.6">
									<div style="font-size:14px;"><b data-i18n="products.items.0.fields.partno"></b>：<span data-i18n="products.items.0.desc.desc_partno"></span></div>
									<div style="font-size:14px; margin-top:10px;"><b data-i18n="products.items.0.fields.basic"></b>：<span data-i18n="products.items.0.desc.desc_basic"></span></div>
									<div style="font-size:14px; margin-top:10px;"><b data-i18n="products.items.0.fields.cells"></b>：<span data-i18n="products.items.0.desc.desc_cells"></span></div>
								</div>
                      </div>
                      <div style="display:flex;align-items:flex-start; margin-top:10px;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 产品2：国产特级 FBS -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/products/new-product3-side.webp"
                              alt="" data-i18n="products.items.1.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Front-Biomed-Superior-Grade-Fetal-Bovine-Serum" data-i18n="products.items.1.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
								<div style="flex:1;margin-left:20px;font-size:14px;line-height:1.6">
									<div style="font-size:14px;">
										<b data-i18n="products.items.1.fields.partno"></b>：
										<span data-i18n="products.items.1.desc.desc_partno"></span>
									</div>
									<div style="font-size:14px; margin-top:10px;">
										<b data-i18n="products.items.1.fields.basic"></b>：
										<span data-i18n="products.items.1.desc.desc_basic"></span>
									</div>
									<div style="font-size:14px; margin-top:10px;">
										<b data-i18n="products.items.1.fields.cells"></b>：
										<span data-i18n="products.items.1.desc.desc_cells"></span>
									</div>
								</div>
                      </div>
                      <div style="display:flex;align-items:flex-start; margin-top:10px;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 产品3：超优级 FBS -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/products/new-product2-side.webp"
                              alt="" data-i18n="products.items.2.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Front-Biomed-Exceptional" data-i18n="products.items.2.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
								<div style="flex:1;margin-left:20px;font-size:14px;line-height:1.6">
									<div style="font-size:14px;">
										<b data-i18n="products.items.2.fields.partno"></b>：
										<span data-i18n="products.items.2.desc.desc_partno"></span>
									</div>
									<div style="font-size:14px; margin-top:10px;">
										<b data-i18n="products.items.2.fields.basic"></b>：
										<span data-i18n="products.items.2.desc.desc_basic"></span>
									</div>
									<div style="font-size:14px; margin-top:10px;">
										<b data-i18n="products.items.2.fields.cells"></b>：
										<span data-i18n="products.items.2.desc.desc_cells"></span>
									</div>
								</div>
                      </div>
                      <div style="display:flex;align-items:flex-start; margin-top:10px;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 产品4：优级 FBS -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/products/guochanteji-side.webp"
                              alt="" data-i18n="products.items.3.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Front-Biomed-Premium-FBS" data-i18n="products.items.3.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
								<div style="flex:1;margin-left:20px;font-size:14px;line-height:1.6">
								<div style="font-size:14px;">
									<b data-i18n="products.items.3.fields.partno"></b>：
									<span data-i18n="products.items.3.desc.desc_partno"></span>
								</div>
								<div style="font-size:14px; margin-top:10px;">
									<b data-i18n="products.items.3.fields.basic"></b>：
									<span data-i18n="products.items.3.desc.desc_basic"></span>
								</div>
								<div style="font-size:14px; margin-top:10px;">
									<b data-i18n="products.items.3.fields.cells"></b>：
									<span data-i18n="products.items.3.desc.desc_cells"></span>
								</div>
								</div>
                      </div>
                      <div style="display:flex;align-items:flex-start; margin-top:10px;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 产品5：新生牛血清 NBCS -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/products/new-product4-side.webp"
                              alt="" data-i18n="products.items.4.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Newborn-Calf-Serum" data-i18n="products.items.4.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
								<div style="flex:1;margin-left:20px;font-size:14px;line-height:1.6">
								<div style="font-size:14px;">
									<b data-i18n="products.items.4.fields.partno"></b>：
									<span data-i18n="products.items.4.desc.desc_partno"></span>
								</div>
								<div style="font-size:14px; margin-top:10px;">
									<b data-i18n="products.items.4.fields.basic"></b>：
									<span data-i18n="products.items.4.desc.desc_basic"></span>
								</div>
								<div style="font-size:14px; margin-top:10px;">
									<b data-i18n="products.items.4.fields.scope"></b>：
									<span data-i18n="products.items.4.desc.desc_scope"></span>
								</div>
								<div style="font-size:14px; margin-top:10px;">
									<b data-i18n="products.items.4.fields.features"></b>：
									<span data-i18n="products.items.4.desc.desc_features"></span>
								</div>
								<div style="font-size:14px; margin-top:10px;">
									<b data-i18n="products.items.4.fields.storage"></b>：
									<span data-i18n="products.items.4.desc.desc_storage"></span>
								</div>
								</div>
                      </div>
                      <div style="display:flex;align-items:flex-start; margin-top:10px;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 产品6：猪血清 -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/animal-product1.webp"
                              alt="" data-i18n="products.items.5.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Pig-Serum" data-i18n="products.items.5.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
                        <p style="flex:1;margin-left:20px;font-size:14px" data-i18n="products.items.5.desc"></p>
                      </div>
                      <div style="display:flex;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.1000"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.3500"></button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 产品7：供体马血清 -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/animal-product2.webp"
                              alt="" data-i18n="products.items.6.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Horse-Serum" data-i18n="products.items.6.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
                        <p style="flex:1;margin-left:20px;font-size:14px" data-i18n="products.items.6.desc"></p>
                      </div>
                      <div style="display:flex;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.1000"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.3500"></button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 产品8：供体山羊血清 -->
                <div class="col-lg-12 col-md-12 prod-row">
                  <div class="d-flex align-items-start">
                    <div class="prod-thumb">
                      <a><img class="lazy rounded" data-src="images/animal-product3.webp"
                              alt="" data-i18n="products.items.7.title" data-i18n-attr="alt"></a>
                    </div>
                    <div class="dlab-post-title" style="flex:1;">
                      <p class="post-title" style="font-size:20px;color:#000;font-weight:600;">
                        <a href="products/Goat-Serum" data-i18n="products.items.7.title"></a>
                      </p>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.overview"></button>
                        <p style="flex:1;margin-left:20px;font-size:14px" data-i18n="products.items.7.desc"></p>
                      </div>
                      <div style="display:flex;align-items:flex-start;">
                        <button class="site-button orange radius-xl m-r15" type="button"
                                style="padding:5px 15px;font-size:14px;" data-i18n="products.labels.specs"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="margin-left:20px;padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.500"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.1000"></button>
                        <button class="site-button bg-primary gradient m-r15 sharp-md"
                                style="padding:5px 20px;font-size:14px;"
                                type="button" data-i18n="products.sizes.3500"></button>
                      </div>
                    </div>
                  </div>
                </div>

              </div><!-- row -->
            </div><!-- col -->
          </div><!-- row -->
        </div><!-- container -->
      </div>
    </div>
  </div>

  <!-- Footer -->
  <?php include 'footer.php'; ?>
  <button class="scroltop fas fa-chevron-up" ></button>
</div>

<!-- JS -->
<script src="js/jquery.min.js"></script>
<script src="plugins/wow/wow.js"></script>
<script src="js/jquery.lazy.min.js"></script>
<script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="plugins/bootstrap-select/bootstrap-select.min.js"></script>
<script src="plugins/bootstrap-touchspin/jquery.bootstrap-touchspin.js"></script>
<script src="plugins/magnific-popup/magnific-popup.js"></script>
<script src="plugins/counter/waypoints-min.js"></script>
<script src="plugins/counter/counterup.min.js"></script>
<script src="plugins/imagesloaded/imagesloaded.js"></script>
<script src="plugins/masonry/masonry-3.1.4.js"></script>
<script src="plugins/masonry/masonry.filter.js"></script>
<script src="plugins/owl-carousel/owl.carousel.js"></script>
<script src="plugins/lightgallery/js/lightgallery-all.min.js"></script>
<script src="plugins/scroll/scrollbar.min.js"></script>
<script src="js/custom.js"></script>
<script src="js/dz.carousel.min.js"></script>
<script src="plugins/countdown/jquery.countdown.js"></script>
<script src="js/dz.ajax.js"></script>

<script>
(function () {
  function getLang() {
    var url = new URL(window.location.href);
    var urlLang = url.searchParams.get('lang');
    var savedLang = localStorage.getItem('lang');
    return (urlLang || savedLang || document.documentElement.getAttribute('lang') || 'zh').toLowerCase();
  }

  // 初始化 lang
  var lang = getLang();
  if (document.documentElement.getAttribute('lang') !== lang) {
    document.documentElement.setAttribute('lang', lang);
  }
  localStorage.setItem('lang', lang);

  // 语言下拉点击：仅当切换到不同语言时才刷新
  function onPick(e) {
    e.preventDefault();
    var picked = this.getAttribute('data-lang');
    if (!picked || picked === lang) return;
    localStorage.setItem('lang', picked);
    var u = new URL(window.location.href);
    u.searchParams.set('lang', picked);
    window.location.href = u.toString();
  }

  // 绑定事件
  var langLinks = document.querySelectorAll('a[data-lang]');
  langLinks.forEach(function (a) { a.addEventListener('click', onPick); });

  // 更新按钮文案
  var toggle = document.getElementById('langToggle');
  if (toggle) {
    toggle.firstChild && (toggle.firstChild.nodeValue = (lang === 'en' ? 'English' : '中文') + ' ');
  }

  // 暴露一个获取当前语言的函数，给下面的 i18n loader 用
  window.__getLang = getLang;
})();
</script>

<script>
  // 小工具
  function deepGet(obj, path) {
    return path.split('.').reduce((o, k) => (o && o[k] !== undefined ? o[k] : null), obj);
  }

  async function loadI18n(lang) {
    const pagePath   = `content/product-center.${lang}.json`;
    const headerPath = `content/header.${lang}.json`;
	const footerPath = `content/footer.${lang}.json`;

    // 并行拉取，任何一个缺失都回退到 zh 的对应文件
    let [pageDict, headerDict, footerDict] = await Promise.allSettled([
      fetch(pagePath, { cache: 'no-cache' }).then(r => { if(!r.ok) throw 0; return r.json(); }),
      fetch(headerPath, { cache: 'no-cache' }).then(r => { if(!r.ok) throw 0; return r.json(); }),
	  fetch(footerPath, { cache: 'no-cache' }).then(r => { if(!r.ok) throw 0; return r.json(); }),
    ]).then(async (results) => {
      let p = results[0].status === 'fulfilled' ? results[0].value : null;
      let h = results[1].status === 'fulfilled' ? results[1].value : null;
	  let f = results[2].status === 'fulfilled' ? results[2].value : null;

      // 各自独立兜底
      if (!p) {
        const r = await fetch(`content/product-center.zh.json`, { cache: 'no-cache' });
        p = r.ok ? await r.json() : {};
      }
      if (!h) {
        const r = await fetch(`content/header.zh.json`, { cache: 'no-cache' });
        h = r.ok ? await r.json() : {};
      }
      if (!f) {
        const r = await fetch(`content/footer.zh.json`, { cache: 'no-cache' });
        f = r.ok ? await r.json() : {};
      }
      return [p, h, f];
    });

    // 选择器：以 "header." 开头的 key 走 headerDict，其余走 pageDict
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const fullKey = el.getAttribute('data-i18n');
      const attr    = el.getAttribute('data-i18n-attr');

      let val = null;
      if (fullKey.startsWith('header.')) {
        // 去掉前缀，在 header.json 内部查找
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
        el.textContent = val;
      }
    });

    // 同步 <title>
    const titleEl = document.querySelector('title[data-i18n="meta.title"]');
    if (titleEl) document.title = titleEl.textContent || document.title;

    // 如果 header.json 里有语言按钮文案，顺便更新下拉按钮显示
    const toggle = document.getElementById('langToggle');
    if (toggle) {
      const label = deepGet(headerDict, 'lang.toggle');
      if (label) {
        // 只替换文字部分，保留 <i> 图标
        const icon = toggle.querySelector('i');
        toggle.innerHTML = '';
        toggle.append(document.createTextNode(label + ' '));
        if (icon) toggle.appendChild(icon);
      }
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    const lang = (window.__getLang ? window.__getLang() : (document.documentElement.getAttribute('lang') || 'zh')).toLowerCase();
    loadI18n(lang);
    if (window.$ && $.fn.lazy) { $('.lazy').Lazy(); }
  });
</script>

</body>
</html>
