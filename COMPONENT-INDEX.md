# Index des composants — ElegantFin Cinema Edition v1.3.14

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.14.css` — 7443 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 420–502, 740, 857, 1503–1523, 2113–2146, 2173–2177, 2453–2471, 2507, 6415, 6673–6689, 6767–6789, 6819–6826, 6916, 7321 |
| `cardScalable` | 28 | 13 | 420–431, 479–502, 803–847, 873–911, 2471, 3476, 3587, 3666, 5608, 6429–6439, 6508, 6673, 6810–6826 |
| `itemDetailPage` | 21 | 13 | 1566, 1652, 1731, 1758, 1986–2022, 2057–2072, 2108, 2209, 2520, 3921–3932, 4420, 4707, 7149–7187 |
| `material-icons` | 17 | 13 | 356–375, 1722, 1820, 1872, 3433, 3592, 3666–3672, 3778, 3936, 4326, 4810, 4844–4854, 5426 |
| `cardImageContainer` | 22 | 12 | 474, 825, 853–882, 911, 968–998, 5733–5737, 5817, 6421, 6500–6508, 6548, 6673–6689, 6810 |
| `skinHeader` | 16 | 10 | 284, 4151, 4184–4211, 5616, 6026, 6082–6090, 6116–6141, 6491, 6640, 7258 |
| `nameContainer` | 27 | 9 | 686, 2216–2239, 2280, 2309, 2344–2390, 2427, 2458–2462, 5183–5235, 7149–7187 |
| `js` | 9 | 9 | 323, 1638, 1731, 2280, 2884, 3566, 5426, 6592, 6836 |
| `card-hoverable` | 23 | 8 | 502, 813, 873–961, 5737, 6439, 6548–6583, 6673, 6962 |
| `parentName` | 23 | 8 | 686, 2221–2239, 2280, 2309, 2344–2390, 5189–5235, 5308, 7149–7187 |
| `detailLogo` | 20 | 8 | 686, 1996–2022, 2057–2072, 2099–2108, 2209–2239, 2309, 2344–2390, 2458 |
| `detailPageWrapperContainer` | 17 | 8 | 686, 1534–1544, 2022, 2182, 2216–2239, 2309, 2344–2390, 2458 |
| `subtitle` | 16 | 8 | 1986–1996, 2108, 2221, 2280, 2399–2409, 2520, 5243–5276, 7149–7187 |
| `backdropCard` | 12 | 8 | 955–961, 1076, 1986–1996, 2125, 2209, 2462–2471, 2498, 2807 |
| `cardBox` | 12 | 8 | 420–468, 494, 740, 895, 1002, 6415, 6673, 6962 |
| `emby-button` | 11 | 8 | 612–629, 656–674, 3146, 3207–3214, 3612, 3647, 3800, 4344 |
| `loginPage` | 16 | 7 | 3745, 5620–5651, 5690, 5718–5737, 6444, 6487, 6799–6826 |
| `nowPlayingBar` | 7 | 7 | 3070, 5869, 6454, 6542, 6626, 6652, 6921 |
| `listItem` | 17 | 6 | 302, 629, 2475, 4246–4272, 4303–4335, 6939–6956 |
| `navMenuOption` | 12 | 6 | 629, 725–735, 3986, 4313–4335, 4401–4406, 6712–6723 |
| `paper-icon-button-light` | 11 | 6 | 574–629, 1652, 1722, 1820, 3373–3393, 5102 |
| `verticalSection` | 11 | 6 | 1726, 2709–2714, 4707, 6500, 6592, 6836 |
| `button-link` | 10 | 6 | 629, 656–674, 3020–3029, 3090–3100, 3146, 7112 |
| `person` | 8 | 6 | 1986–2007, 2209, 2462, 2507–2516, 3873, 7144 |
| `mainDrawer` | 7 | 6 | 3034, 3950, 4184, 6444–6454, 6699, 6738 |
| `detailImageContainer` | 20 | 5 | 1986–2007, 2113–2177, 2209, 2449–2471, 2498–2516 |
| `osdHeader` | 15 | 5 | 1695–1713, 6021–6090, 6116–6141, 6491, 6921 |
| `actionSheetMenuItem` | 11 | 5 | 629, 4246–4257, 4303, 4381–4397, 6472 |
| `sectionTabs` | 10 | 5 | 1789, 3724, 4211, 6062–6067, 6207–6233 |
| `cardImageIcon` | 8 | 5 | 412–416, 2462–2471, 2534, 3460, 5817 |
| `headerTop` | 8 | 5 | 4151, 4184, 6032–6057, 6108–6125, 6152–6156 |
| `sectionTitle` | 7 | 5 | 1726, 1799–1806, 4052, 4780–4788, 5685 |
| `emby-scroller-container` | 6 | 5 | 1726–1731, 1769, 2699, 6500, 6592 |
| `portraitCard` | 6 | 5 | 1076, 1154, 1910–1915, 2173, 2807 |
| `scss` | 5 | 5 | 284, 768, 1028, 3482, 6592 |
| `skinHeader-withBackground` | 5 | 5 | 1634, 3921, 5616, 6021, 6071 |
| `btnPlay` | 16 | 4 | 511–535, 574–629, 3676–3718, 3751–3778 |
| `cardOverlayContainer` | 12 | 4 | 929–961, 1006–1028, 1088, 6921–6939 |
| `itemName` | 11 | 4 | 686, 2280, 5189–5235, 5326–5343 |
| `backdropImage` | 10 | 4 | 2599–2626, 2653–2657, 6408, 6508–6516 |
| `emby-tab-button` | 10 | 4 | 629, 696–705, 3724, 6192–6228 |
| `upNextContainer` | 10 | 4 | 4872–4891, 4917–4943, 6444–6454, 6480 |
| `emby-scroller` | 9 | 4 | 1731, 1769–1775, 6742–6789, 6900–6916 |
| `backgroundContainer` | 8 | 4 | 2076, 2590, 2631–2649, 2681 |
| `detailRibbon` | 8 | 4 | 1591–1619, 1825, 1910–1922, 7144 |
| `listItemBodyText` | 7 | 4 | 4267–4286, 4326, 4385, 6956 |
| `visualCardBox` | 7 | 4 | 420, 834–847, 873–878, 1002 |
| `button-submit` | 6 | 4 | 3745, 3832, 5718–5726, 7024–7038 |
| `cardText-secondary` | 6 | 4 | 302, 916, 3465–3469, 6570–6578 |
| `detailPagePrimaryContent` | 6 | 4 | 1606–1624, 2414, 4701, 6656 |
| `skip-button` | 6 | 4 | 629, 3729, 4966–4983, 5010–5016 |
| `squareCard` | 6 | 4 | 857, 2462, 2498–2516, 5694–5698 |
| `skinHeader-blurred` | 5 | 4 | 5616, 6050–6057, 6640, 6921 |
| `appfooter` | 4 | 4 | 2750, 6166, 6531, 6921 |
| `itemsContainer` | 4 | 4 | 740, 1758, 1793, 4707 |
| `raised` | 4 | 4 | 629, 715, 3612, 3647 |
| `detailButton` | 13 | 3 | 574–629, 3657–3718, 3774–3778 |
| `itemSelectionPanel` | 9 | 3 | 886–890, 3405, 3433–3476 |
| `check` | 8 | 3 | 3433, 3666, 4377–4397 |
| `pageTitle` | 8 | 3 | 1670–1713, 6082, 6141 |
| `sectionTitleTextButton` | 8 | 3 | 4763–4771, 4798–4810, 4844–4854 |
| `homePage` | 7 | 3 | 4151, 4184–4211, 6250 |
| `playedIndicator` | 7 | 3 | 768–782, 3549, 6673–6694 |
| `detailSectionContent` | 6 | 3 | 3239, 4502–4512, 4592–4602 |
| `emby-checkbox` | 6 | 3 | 3410, 3447–3451, 3500–3512 |
| `actionSheetContent` | 5 | 3 | 4369–4373, 6444–6454, 6480 |
| `cardText-first` | 5 | 3 | 916, 3439–3465, 5798 |
| `dialog` | 5 | 3 | 3289–3299, 6444–6454, 6480 |
| `guideProgramName` | 5 | 3 | 629, 5367–5378, 5421–5426 |
| `noHomeButtonHeader` | 5 | 3 | 1652, 6082, 6192–6200 |
| `overflowBackdropCard` | 5 | 3 | 955–961, 3443, 5793–5798 |
| `secondary` | 5 | 3 | 302, 4276–4286, 4326 |
| `album` | 4 | 3 | 2209, 2467–2471, 2507 |
| `cardPadder` | 4 | 3 | 416, 1002, 3456–3460 |
| `cardText` | 4 | 3 | 916–926, 3465, 6815 |
| `detailPageContent` | 4 | 3 | 1748, 4433, 4694–4701 |
| `dialog-fullscreen` | 4 | 3 | 3299, 6444–6454, 6480 |
| `emby-scrollbuttons` | 4 | 3 | 1811–1816, 6836, 7296 |
| `folder` | 4 | 3 | 1910–1915, 3566, 3630 |
| `formDialogFooter` | 4 | 3 | 3357, 3839, 6973–6997 |
| `infoWrapper` | 4 | 3 | 2152–2157, 2414, 2442 |
| `listItemImage` | 4 | 3 | 2784–2789, 4240, 6956 |
| `musicParentName` | 4 | 3 | 1986, 2520, 5308–5317 |
| `semiTransparent` | 4 | 3 | 1634, 5616, 6050–6071 |
| `toast` | 4 | 3 | 4864, 6444–6454, 6480 |
| `cardFooter` | 3 | 3 | 3476, 6548, 6583 |
| `defaultCardBackground` | 3 | 3 | 3587, 5813, 5912 |
| `detailPageSecondaryContainer` | 3 | 3 | 1601, 1628, 1748 |
| `formDialogFooterItem` | 3 | 3 | 3357, 3625, 3751 |
| `formDialogHeader` | 3 | 3 | 3839, 6921, 6973 |
| `iconOsd` | 3 | 3 | 5594, 6921, 6973 |
| `live_tv` | 3 | 3 | 1986, 2507, 3873 |
| `myPreferencesMenuPage` | 3 | 3 | 389, 4411, 4715 |
| `page` | 3 | 3 | 998, 2681, 6500 |
| `playerStats` | 3 | 3 | 5594, 6973, 7009 |
| `sectionTitle-cards` | 3 | 3 | 1726, 4780, 4840 |
| `sectionTitleContainer` | 3 | 3 | 1758, 1816, 4626 |
| `x` | 3 | 3 | 2280, 5291, 6592 |
| `itemExternalLinks` | 13 | 2 | 3083–3161, 3239 |
| `checkboxOutline` | 10 | 2 | 3410–3451, 3482–3512 |
| `itemBackdrop` | 9 | 2 | 1952–2007, 2182 |
| `mdl-slider` | 9 | 2 | 2880, 2935–2993 |
| `listItemIcon` | 8 | 2 | 3869–3873, 4381–4411 |
| `sliderContainer` | 8 | 2 | 2884, 2912–2977 |
| `cardOverlayButton-br` | 7 | 2 | 1014, 1043–1081 |
| `detail-clamp-text` | 7 | 2 | 3175–3201, 3227–3231 |
| `divUsers` | 7 | 2 | 5694–5698, 6799–6826 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3447–3451, 3481–3500 |
| `countIndicator` | 6 | 2 | 759–789, 6973–6997 |
| `detailPagePrimaryContainer` | 6 | 2 | 1578–1624, 2414 |
| `detailsGroupItem` | 6 | 2 | 4464, 4532–4569 |
| `headerButton` | 6 | 2 | 549–629, 6134 |
| `headerLeft` | 6 | 2 | 1676–1713, 6337 |
| `selectionCommandsPanel` | 6 | 2 | 3367–3401, 6921 |
| `trackSelections` | 6 | 2 | 4437–4464, 4597–4602 |
| `withBackdrop` | 6 | 2 | 2590, 2631–2649 |
| `detailSection` | 5 | 2 | 4420–4429, 4582–4602 |
| `fullSyncIndicator` | 5 | 2 | 759–782, 6973–6997 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3043, 6712–6729 |
| `mediaInfoItem` | 5 | 2 | 1829–1872, 6592 |
| `overview-expand` | 5 | 2 | 3207–3231, 4502 |
| `scrollX` | 5 | 2 | 1731, 1769–1789 |
| `videoIndicator` | 5 | 2 | 3555–3583, 6973 |
| `withSectionTabs` | 5 | 2 | 2640–2657, 6057 |
| `alphaPickerButton` | 4 | 2 | 629, 4641–4653 |
| `backgroundProgress` | 4 | 2 | 2795–2807, 2837 |
| `emby-tab-button-active` | 4 | 2 | 3811, 6219–6233 |
| `mediaSourceIndicator` | 4 | 2 | 759–782, 6973 |
| `play_arrow` | 4 | 2 | 3592–3608, 3778 |
| `playbackProgress` | 4 | 2 | 2795–2807, 2842 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4267–4272, 5906–5912 |
| `programCell` | 4 | 2 | 5358, 5417–5426 |
| `programGuideSection` | 4 | 2 | 2475–2490, 4602–4617 |
| `section0` | 4 | 2 | 968–998, 6500 |
| `visualLoginForm` | 4 | 2 | 5685–5702, 5743 |
| `cardOverlayButtonIcon` | 3 | 2 | 1014–1026, 1081 |
| `castCollapsible` | 3 | 2 | 825, 3451–3460 |
| `collectionItems` | 3 | 2 | 1758, 4602–4626 |
| `emby-input` | 3 | 2 | 5116–5132, 7038 |
| `emby-scrollbuttons-button` | 3 | 2 | 1820, 7303–7310 |
| `guestCastContent` | 3 | 2 | 825, 3451–3460 |
| `guide-channelHeaderCell` | 3 | 2 | 629, 5392–5408 |
| `guide-date-tab-button` | 3 | 2 | 629, 3811–3819 |
| `headerUserButton` | 3 | 2 | 549–562, 4719 |
| `manualLoginForm` | 3 | 2 | 5685–5702, 5743 |
| `overview` | 3 | 2 | 3227–3231, 4512 |
| `add` | 2 | 2 | 1731, 6592 |
| `alphaPicker-fixed-right` | 2 | 2 | 2681, 4653 |
| `backdropImageFadeIn` | 2 | 2 | 2734, 7013 |
| `book` | 2 | 2 | 1986, 2507 |
| `btnDeleteImage` | 2 | 2 | 3612, 3825 |
| `cardContent` | 2 | 2 | 825, 857 |
| `cardOverlayButton` | 2 | 2 | 1028, 1064 |
| `cardOverlayButton-hover` | 2 | 2 | 911, 1043 |
| `chevron_right` | 2 | 2 | 4810, 4854 |
| `classList` | 2 | 2 | 1731, 6592 |
| `collapseContent` | 2 | 2 | 3362, 3837 |
| `collectionItemsContainer` | 2 | 2 | 1758, 4630 |
| `content-primary` | 2 | 2 | 4694, 4746 |
| `editorsChoiceItemOverview` | 2 | 2 | 7233, 7314 |
| `emby-select` | 2 | 2 | 5116, 7038 |
| `endsAt` | 2 | 2 | 1850, 6592 |
| `fieldDescription` | 2 | 2 | 302, 7038 |
| `formDialogFooter-clear` | 2 | 2 | 3357, 3839 |
| `guide-programNameCaret` | 2 | 2 | 302, 5374 |
| `headroom` | 2 | 2 | 6045, 6082 |
| `indicator` | 2 | 2 | 789, 3544 |
| `mediaInfoOfficialRating` | 2 | 2 | 1850, 6592 |
| `navMenuOption-selected` | 2 | 2 | 4416, 6723 |
| `nowPlayingInfoContainer` | 2 | 2 | 3074, 5843 |
| `org` | 2 | 2 | 3110, 3140 |
| `paperList` | 2 | 2 | 834, 3850 |
| `playlist` | 2 | 2 | 4262, 5821 |
| `programSecondaryTitle` | 2 | 2 | 302, 5426 |
| `queue` | 2 | 2 | 1986, 2507 |
| `readOnlyContent` | 2 | 2 | 3881, 6266 |
| `recordingFields` | 2 | 2 | 4456, 4597 |
| `runtime` | 2 | 2 | 5755, 5783 |
| `sectionTitleContainer-cards` | 2 | 2 | 4775, 4840 |
| `sidebarHeader` | 2 | 2 | 3973, 6729 |
| `tagline` | 2 | 2 | 2581, 4512 |
| `tsx` | 2 | 2 | 4151, 4215 |
| `upNextDialog-title` | 2 | 2 | 4896, 4930 |
| `vertical-list` | 2 | 2 | 1793, 7139 |
| `vertical-wrap` | 2 | 2 | 755, 1758 |
| `videoOsdBottom` | 2 | 2 | 3066, 6012 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3066, 6012 |
| `userPreferencesPage` | 12 | 1 | 7024–7119 |
| `checkboxContainer` | 7 | 1 | 3439–3476 |
| `itemDetailsGroup` | 7 | 1 | 4516–4602 |
| `itemProgressBar` | 6 | 1 | 2784–2818 |
| `trackSelectionFieldContainer` | 6 | 1 | 4475–4498 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7270–7310 |
| `innerCardFooter` | 5 | 1 | 3252–3281 |
| `chapterCardImageContainer` | 4 | 1 | 3252–3281 |
| `endTimeText` | 4 | 1 | 5755–5783 |
| `mainDetailButtons` | 4 | 1 | 3774–3788 |
| `overview-controls` | 4 | 1 | 3227–3239 |
| `startTimeText` | 4 | 1 | 5755–5777 |
| `button-flat` | 3 | 1 | 3047–3057 |
| `cardIndicators` | 3 | 1 | 3529–3539 |
| `cardOverlayFab-primary` | 3 | 1 | 1006–1028 |
| `com` | 3 | 1 | 3116–3134 |
| `content` | 3 | 1 | 4538–4569 |
| `discover-card` | 3 | 1 | 7321–7344 |
| `emby-select-withcolor` | 3 | 1 | 5116–5150 |
| `emby-textarea` | 3 | 1 | 5107–5132 |
| `fab` | 3 | 1 | 3634–3647 |
| `listChildrenCollapsible` | 3 | 1 | 4587–4602 |
| `mdl-slider-background-flex` | 3 | 1 | 2904–2917 |
| `mediaInfoCriticRating` | 3 | 1 | 1891–1900 |
| `nextUpSection` | 3 | 1 | 4582–4602 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5807–5817 |
| `serverInfo` | 3 | 1 | 3854–3863 |
| `transcodingProgress` | 3 | 1 | 2795–2807 |
