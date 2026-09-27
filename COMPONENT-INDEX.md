# Index des composants — ElegantFin Cinema Edition v1.3.10

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.10.css` — 7312 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 416–498, 736, 839, 1485–1505, 2027–2060, 2087–2091, 2367–2385, 2421, 6291, 6549–6565, 6643–6665, 6695–6702, 6785, 7190 |
| `cardScalable` | 28 | 13 | 416–427, 475–498, 785–829, 855–893, 2385, 3368, 3479, 3558, 5500, 6305–6315, 6384, 6549, 6686–6702 |
| `material-icons` | 17 | 13 | 352–371, 1704, 1782, 1834, 3325, 3484, 3558–3564, 3670, 3828, 4218, 4702, 4736–4746, 5318 |
| `cardImageContainer` | 22 | 12 | 470, 807, 835–864, 893, 950–980, 5609–5613, 5693, 6297, 6376–6384, 6424, 6549–6565, 6686 |
| `itemDetailPage` | 18 | 11 | 1548, 1634, 1713, 1953–1978, 2022, 2123, 2434–2439, 3813–3824, 4312, 4599, 7018–7056 |
| `skinHeader` | 16 | 10 | 280, 4043, 4076–4103, 5508, 5902, 5958–5966, 5992–6017, 6367, 6516, 7127 |
| `nameContainer` | 27 | 9 | 682, 2130–2153, 2194, 2223, 2258–2304, 2341, 2372–2376, 5075–5127, 7018–7056 |
| `backdropCard` | 12 | 9 | 937–943, 1058, 1953, 2039, 2123, 2376–2385, 2412, 2439, 2719 |
| `js` | 9 | 9 | 319, 1620, 1713, 2194, 2796, 3458, 5318, 6468, 6712 |
| `card-hoverable` | 23 | 8 | 498, 795, 855–943, 5613, 6315, 6424–6459, 6549, 6831 |
| `parentName` | 23 | 8 | 682, 2135–2153, 2194, 2223, 2258–2304, 5081–5127, 5200, 7018–7056 |
| `detailPageWrapperContainer` | 17 | 8 | 682, 1516–1526, 1978, 2096, 2130–2153, 2223, 2258–2304, 2372 |
| `subtitle` | 16 | 8 | 1953, 2022, 2135, 2194, 2313–2323, 2434–2439, 5135–5168, 7018–7056 |
| `cardBox` | 12 | 8 | 416–464, 490, 736, 877, 984, 6291, 6549, 6831 |
| `emby-button` | 11 | 8 | 608–625, 652–670, 3058, 3127–3134, 3504, 3539, 3692, 4236 |
| `detailLogo` | 17 | 7 | 682, 1967–1978, 2013–2022, 2123–2153, 2223, 2258–2304, 2372 |
| `loginPage` | 15 | 7 | 3637, 5512–5527, 5566, 5594–5613, 6320, 6363, 6675–6702 |
| `nowPlayingBar` | 7 | 7 | 2982, 5745, 6330, 6418, 6502, 6528, 6790 |
| `listItem` | 17 | 6 | 298, 625, 2389, 4138–4164, 4195–4227, 6808–6825 |
| `navMenuOption` | 12 | 6 | 625, 721–731, 3878, 4205–4227, 4293–4298, 6588–6599 |
| `verticalSection` | 11 | 6 | 1708, 2620–2625, 4599, 6376, 6468, 6712 |
| `button-link` | 10 | 6 | 625, 652–670, 2932–2941, 3002–3012, 3058, 6981 |
| `person` | 8 | 6 | 1953–1963, 2123, 2376, 2421–2430, 3765, 7013 |
| `mainDrawer` | 7 | 6 | 2946, 3842, 4076, 6320–6330, 6575, 6614 |
| `detailImageContainer` | 20 | 5 | 1953–1963, 2027–2091, 2123, 2363–2385, 2412–2439 |
| `osdHeader` | 15 | 5 | 1677–1695, 5897–5966, 5992–6017, 6367, 6790 |
| `actionSheetMenuItem` | 11 | 5 | 625, 4138–4149, 4195, 4273–4289, 6348 |
| `sectionTabs` | 10 | 5 | 1751, 3616, 4103, 5938–5943, 6083–6109 |
| `cardImageIcon` | 8 | 5 | 408–412, 2376–2385, 2445, 3352, 5693 |
| `headerTop` | 8 | 5 | 4043, 4076, 5908–5933, 5984–6001, 6028–6032 |
| `paper-icon-button-light` | 8 | 5 | 570–625, 1634, 1704, 1782, 4994 |
| `sectionTitle` | 7 | 5 | 1708, 1761–1768, 3944, 4672–4680, 5561 |
| `emby-scroller-container` | 6 | 5 | 1708–1713, 1740, 2610, 6376, 6468 |
| `portraitCard` | 5 | 5 | 1058, 1136, 1872, 2087, 2719 |
| `scss` | 5 | 5 | 280, 764, 1010, 3374, 6468 |
| `skinHeader-withBackground` | 5 | 5 | 1616, 3813, 5508, 5897, 5947 |
| `btnPlay` | 16 | 4 | 507–531, 570–625, 3568–3610, 3643–3670 |
| `cardOverlayContainer` | 12 | 4 | 911–943, 988–1010, 1070, 6790–6808 |
| `itemName` | 11 | 4 | 682, 2194, 5081–5127, 5218–5235 |
| `backdropImage` | 10 | 4 | 2510–2537, 2564–2568, 6284, 6384–6392 |
| `emby-tab-button` | 10 | 4 | 625, 692–701, 3616, 6068–6104 |
| `upNextContainer` | 10 | 4 | 4764–4783, 4809–4835, 6320–6330, 6356 |
| `emby-scroller` | 9 | 4 | 1713, 1740–1746, 6618–6665, 6776–6785 |
| `detailRibbon` | 7 | 4 | 1573–1601, 1787, 1872–1877, 7013 |
| `listItemBodyText` | 7 | 4 | 4159–4178, 4218, 4277, 6825 |
| `visualCardBox` | 7 | 4 | 416, 816–829, 855–860, 984 |
| `button-submit` | 6 | 4 | 3637, 3724, 5594–5602, 6893–6907 |
| `cardText-secondary` | 6 | 4 | 298, 898, 3357–3361, 6446–6454 |
| `detailPagePrimaryContent` | 6 | 4 | 1588–1606, 2328, 4593, 6532 |
| `skip-button` | 6 | 4 | 625, 3621, 4858–4875, 4902–4908 |
| `squareCard` | 6 | 4 | 839, 2376, 2412–2430, 5570–5574 |
| `skinHeader-blurred` | 5 | 4 | 5508, 5926–5933, 6516, 6790 |
| `appfooter` | 4 | 4 | 2662, 6042, 6407, 6790 |
| `raised` | 4 | 4 | 625, 711, 3504, 3539 |
| `detailButton` | 13 | 3 | 570–625, 3549–3610, 3666–3670 |
| `itemBackdrop` | 9 | 3 | 1919–1963, 2096, 2439 |
| `itemSelectionPanel` | 9 | 3 | 868–872, 3297, 3325–3368 |
| `check` | 8 | 3 | 3325, 3558, 4269–4289 |
| `pageTitle` | 8 | 3 | 1652–1695, 5958, 6017 |
| `sectionTitleTextButton` | 8 | 3 | 4655–4663, 4690–4702, 4736–4746 |
| `backgroundContainer` | 7 | 3 | 2501, 2542–2560, 2592 |
| `homePage` | 7 | 3 | 4043, 4076–4103, 6126 |
| `playedIndicator` | 7 | 3 | 764–778, 3441, 6549–6570 |
| `detailSectionContent` | 6 | 3 | 3159, 4394–4404, 4484–4494 |
| `emby-checkbox` | 6 | 3 | 3302, 3339–3343, 3392–3404 |
| `actionSheetContent` | 5 | 3 | 4261–4265, 6320–6330, 6356 |
| `cardText-first` | 5 | 3 | 898, 3331–3357, 5674 |
| `dialog` | 5 | 3 | 3209–3219, 6320–6330, 6356 |
| `guideProgramName` | 5 | 3 | 625, 5259–5270, 5313–5318 |
| `musicParentName` | 5 | 3 | 1953, 2434–2439, 5200–5209 |
| `noHomeButtonHeader` | 5 | 3 | 1634, 5958, 6068–6076 |
| `overflowBackdropCard` | 5 | 3 | 937–943, 3335, 5669–5674 |
| `secondary` | 5 | 3 | 298, 4168–4178, 4218 |
| `album` | 4 | 3 | 2123, 2381–2385, 2421 |
| `cardPadder` | 4 | 3 | 412, 984, 3348–3352 |
| `cardText` | 4 | 3 | 898–908, 3357, 6691 |
| `detailPageContent` | 4 | 3 | 1730, 4325, 4586–4593 |
| `dialog-fullscreen` | 4 | 3 | 3219, 6320–6330, 6356 |
| `emby-scrollbuttons` | 4 | 3 | 1773–1778, 6712, 7165 |
| `formDialogFooter` | 4 | 3 | 3277, 3731, 6842–6866 |
| `infoWrapper` | 4 | 3 | 2066–2071, 2328, 2356 |
| `listItemImage` | 4 | 3 | 2696–2701, 4132, 6825 |
| `semiTransparent` | 4 | 3 | 1616, 5508, 5926–5947 |
| `toast` | 4 | 3 | 4756, 6320–6330, 6356 |
| `cardFooter` | 3 | 3 | 3368, 6424, 6459 |
| `defaultCardBackground` | 3 | 3 | 3479, 5689, 5788 |
| `detailPageSecondaryContainer` | 3 | 3 | 1583, 1610, 1730 |
| `folder` | 3 | 3 | 1872, 3458, 3522 |
| `formDialogFooterItem` | 3 | 3 | 3277, 3517, 3643 |
| `formDialogHeader` | 3 | 3 | 3731, 6790, 6842 |
| `iconOsd` | 3 | 3 | 5486, 6790, 6842 |
| `itemsContainer` | 3 | 3 | 736, 1755, 4599 |
| `live_tv` | 3 | 3 | 1953, 2421, 3765 |
| `myPreferencesMenuPage` | 3 | 3 | 385, 4303, 4607 |
| `page` | 3 | 3 | 980, 2592, 6376 |
| `playerStats` | 3 | 3 | 5486, 6842, 6878 |
| `sectionTitle-cards` | 3 | 3 | 1708, 4672, 4732 |
| `x` | 3 | 3 | 2194, 5183, 6468 |
| `itemExternalLinks` | 13 | 2 | 2995–3073, 3159 |
| `checkboxOutline` | 10 | 2 | 3302–3343, 3374–3404 |
| `mdl-slider` | 9 | 2 | 2792, 2847–2905 |
| `listItemIcon` | 8 | 2 | 3761–3765, 4273–4303 |
| `sliderContainer` | 8 | 2 | 2796, 2824–2889 |
| `cardOverlayButton-br` | 7 | 2 | 996, 1025–1063 |
| `detail-clamp-text` | 7 | 2 | 3095–3121, 3147–3151 |
| `divUsers` | 7 | 2 | 5570–5574, 6675–6702 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3339–3343, 3373–3392 |
| `detailPagePrimaryContainer` | 6 | 2 | 1560–1606, 2328 |
| `detailsGroupItem` | 6 | 2 | 4356, 4424–4461 |
| `headerButton` | 6 | 2 | 545–625, 6010 |
| `headerLeft` | 6 | 2 | 1658–1695, 6213 |
| `trackSelections` | 6 | 2 | 4329–4356, 4489–4494 |
| `withBackdrop` | 6 | 2 | 2501, 2542–2560 |
| `countIndicator` | 5 | 2 | 755–778, 6842–6866 |
| `detailSection` | 5 | 2 | 4312–4321, 4474–4494 |
| `fullSyncIndicator` | 5 | 2 | 755–778, 6842–6866 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2955, 6588–6605 |
| `mediaInfoItem` | 5 | 2 | 1791–1834, 6468 |
| `overview-expand` | 5 | 2 | 3127–3151, 4394 |
| `videoIndicator` | 5 | 2 | 3447–3475, 6842 |
| `withSectionTabs` | 5 | 2 | 2551–2568, 5933 |
| `alphaPickerButton` | 4 | 2 | 625, 4533–4545 |
| `backgroundProgress` | 4 | 2 | 2707–2719, 2749 |
| `emby-tab-button-active` | 4 | 2 | 3703, 6095–6109 |
| `mediaSourceIndicator` | 4 | 2 | 755–778, 6842 |
| `play_arrow` | 4 | 2 | 3484–3500, 3670 |
| `playbackProgress` | 4 | 2 | 2707–2719, 2754 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4159–4164, 5782–5788 |
| `programCell` | 4 | 2 | 5250, 5309–5318 |
| `programGuideSection` | 4 | 2 | 2389–2404, 4494–4509 |
| `scrollX` | 4 | 2 | 1713, 1740–1751 |
| `section0` | 4 | 2 | 950–980, 6376 |
| `visualLoginForm` | 4 | 2 | 5561–5578, 5619 |
| `cardOverlayButtonIcon` | 3 | 2 | 996–1008, 1063 |
| `castCollapsible` | 3 | 2 | 807, 3343–3352 |
| `emby-input` | 3 | 2 | 5008–5024, 6907 |
| `emby-scrollbuttons-button` | 3 | 2 | 1782, 7172–7179 |
| `guestCastContent` | 3 | 2 | 807, 3343–3352 |
| `guide-channelHeaderCell` | 3 | 2 | 625, 5284–5300 |
| `guide-date-tab-button` | 3 | 2 | 625, 3703–3711 |
| `headerUserButton` | 3 | 2 | 545–558, 4611 |
| `manualLoginForm` | 3 | 2 | 5561–5578, 5619 |
| `overview` | 3 | 2 | 3147–3151, 4404 |
| `selectionCommandsPanel` | 3 | 2 | 3287–3293, 6790 |
| `add` | 2 | 2 | 1713, 6468 |
| `alphaPicker-fixed-right` | 2 | 2 | 2592, 4545 |
| `backdropImageFadeIn` | 2 | 2 | 2646, 6882 |
| `book` | 2 | 2 | 1953, 2421 |
| `btnDeleteImage` | 2 | 2 | 3504, 3717 |
| `cardContent` | 2 | 2 | 807, 839 |
| `cardOverlayButton` | 2 | 2 | 1010, 1046 |
| `cardOverlayButton-hover` | 2 | 2 | 893, 1025 |
| `chevron_right` | 2 | 2 | 4702, 4746 |
| `classList` | 2 | 2 | 1713, 6468 |
| `collapseContent` | 2 | 2 | 3282, 3729 |
| `content-primary` | 2 | 2 | 4586, 4638 |
| `editorsChoiceItemOverview` | 2 | 2 | 7102, 7183 |
| `emby-select` | 2 | 2 | 5008, 6907 |
| `endsAt` | 2 | 2 | 1812, 6468 |
| `fieldDescription` | 2 | 2 | 298, 6907 |
| `formDialogFooter-clear` | 2 | 2 | 3277, 3731 |
| `guide-programNameCaret` | 2 | 2 | 298, 5266 |
| `headroom` | 2 | 2 | 5921, 5958 |
| `mediaInfoOfficialRating` | 2 | 2 | 1812, 6468 |
| `navMenuOption-selected` | 2 | 2 | 4308, 6599 |
| `nowPlayingInfoContainer` | 2 | 2 | 2986, 5719 |
| `org` | 2 | 2 | 3022, 3052 |
| `paperList` | 2 | 2 | 816, 3742 |
| `playlist` | 2 | 2 | 4154, 5697 |
| `programSecondaryTitle` | 2 | 2 | 298, 5318 |
| `queue` | 2 | 2 | 1953, 2421 |
| `readOnlyContent` | 2 | 2 | 3773, 6142 |
| `recordingFields` | 2 | 2 | 4348, 4489 |
| `runtime` | 2 | 2 | 5631, 5659 |
| `sectionTitleContainer` | 2 | 2 | 1778, 4518 |
| `sectionTitleContainer-cards` | 2 | 2 | 4667, 4732 |
| `sidebarHeader` | 2 | 2 | 3865, 6605 |
| `tagline` | 2 | 2 | 2492, 4404 |
| `tsx` | 2 | 2 | 4043, 4107 |
| `upNextDialog-title` | 2 | 2 | 4788, 4822 |
| `vertical-list` | 2 | 2 | 1755, 7008 |
| `videoOsdBottom` | 2 | 2 | 2978, 5888 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2978, 5888 |
| `userPreferencesPage` | 12 | 1 | 6893–6988 |
| `checkboxContainer` | 7 | 1 | 3331–3368 |
| `itemDetailsGroup` | 7 | 1 | 4408–4494 |
| `itemProgressBar` | 6 | 1 | 2696–2730 |
| `trackSelectionFieldContainer` | 6 | 1 | 4367–4390 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7139–7179 |
| `innerCardFooter` | 5 | 1 | 3172–3201 |
| `chapterCardImageContainer` | 4 | 1 | 3172–3201 |
| `endTimeText` | 4 | 1 | 5631–5659 |
| `mainDetailButtons` | 4 | 1 | 3666–3680 |
| `overview-controls` | 4 | 1 | 3147–3159 |
| `startTimeText` | 4 | 1 | 5631–5653 |
| `button-flat` | 3 | 1 | 2959–2969 |
| `cardIndicators` | 3 | 1 | 3421–3431 |
| `cardOverlayFab-primary` | 3 | 1 | 988–1010 |
| `com` | 3 | 1 | 3028–3046 |
| `content` | 3 | 1 | 4430–4461 |
| `discover-card` | 3 | 1 | 7190–7213 |
| `emby-select-withcolor` | 3 | 1 | 5008–5042 |
| `emby-textarea` | 3 | 1 | 4999–5024 |
| `fab` | 3 | 1 | 3526–3539 |
| `listChildrenCollapsible` | 3 | 1 | 4479–4494 |
| `mdl-slider-background-flex` | 3 | 1 | 2816–2829 |
| `mediaInfoCriticRating` | 3 | 1 | 1853–1862 |
| `nextUpSection` | 3 | 1 | 4474–4494 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5683–5693 |
| `serverInfo` | 3 | 1 | 3746–3755 |
| `transcodingProgress` | 3 | 1 | 2707–2719 |
