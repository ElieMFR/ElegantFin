# Index des composants — ElegantFin Cinema Edition v1.2.92

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.2.92.css` — 6215 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 14 | 379–390, 422–434, 612, 694, 1328–1348, 1807–1840, 1867–1871, 2127–2158, 5408, 5692–5708, 5788–5810, 5840, 5912, 6185 |
| `cardScalable` | 25 | 13 | 379–390, 427–434, 640–684, 710–748, 2145, 3040, 3142, 3221, 4712, 5422–5432, 5501, 5692, 5831–5840 |
| `cardImageContainer` | 24 | 13 | 422, 662, 690–719, 748, 805–835, 4821–4825, 4906, 5414, 5493–5501, 5539–5555, 5692–5708, 5831, 5960 |
| `material-icons` | 15 | 11 | 315–334, 1513, 1572, 1624, 3003, 3147, 3221–3227, 3333, 3586, 4021, 4055–4065 |
| `itemDetailPage` | 16 | 10 | 1391, 1464, 1522, 1733–1758, 1802, 1882, 2173–2178, 3680, 3942, 6013–6051 |
| `nameContainer` | 27 | 9 | 571, 1890–1913, 1954, 1983, 2018–2064, 2101, 2132–2136, 4388–4440, 6013–6051 |
| `card-hoverable` | 23 | 8 | 434, 650, 710–798, 4825, 5432, 5566–5585, 5692, 5967 |
| `parentName` | 23 | 8 | 571, 1895–1913, 1954, 1983, 2018–2064, 4394–4440, 4513, 6013–6051 |
| `subtitle` | 16 | 8 | 1733, 1802, 1895, 1954, 2073–2083, 2173–2178, 4448–4481, 6013–6051 |
| `cardBox` | 11 | 8 | 379–390, 416–434, 612, 732, 839, 5408, 5692, 5967 |
| `detailLogo` | 17 | 7 | 571, 1747–1758, 1793–1802, 1882–1913, 1983, 2018–2064, 2132 |
| `detailPageWrapperContainer` | 17 | 7 | 571, 1359–1369, 1758, 1876–1913, 1983, 2018–2064, 2132 |
| `loginPage` | 14 | 7 | 3300, 4724–4739, 4778, 4806–4825, 5437, 5480, 5820–5840 |
| `backdropCard` | 12 | 7 | 792–798, 901, 1733, 1819, 1882, 2136–2178, 2443 |
| `skinHeader` | 11 | 7 | 4720, 5049, 5105–5113, 5139–5164, 5484, 5660, 6122 |
| `emby-button` | 9 | 7 | 508–525, 552, 2802–2809, 3167, 3202, 3355, 3604 |
| `nowPlayingBar` | 8 | 6 | 2687, 4958, 5447, 5526, 5641–5672, 5917 |
| `listItem` | 16 | 5 | 525, 2149, 3504–3530, 3561–3595, 5935–5952 |
| `osdHeader` | 15 | 5 | 1494–1504, 5044–5113, 5139–5164, 5484, 5917 |
| `actionSheetMenuItem` | 11 | 5 | 525, 3504–3515, 3561, 3641–3657, 5465 |
| `emby-scroller-container` | 11 | 5 | 1517–1530, 2334, 2365, 5493, 5595–5623 |
| `navMenuOption` | 11 | 5 | 525, 601–607, 3567–3595, 3661–3666, 5731–5742 |
| `verticalSection` | 10 | 5 | 1517, 2344–2349, 3942, 5493, 5848 |
| `cardImageIcon` | 8 | 5 | 371–375, 2136–2145, 2184, 3030, 4906 |
| `person` | 8 | 5 | 1733–1743, 1882, 2136–2169, 3422, 6008 |
| `portraitCard` | 5 | 5 | 901, 979, 1652, 1867, 2443 |
| `btnPlay` | 14 | 4 | 445, 484–525, 3231–3273, 3306–3333 |
| `cardOverlayContainer` | 12 | 4 | 766–798, 843–863, 913, 5917–5935 |
| `itemName` | 11 | 4 | 571, 1954, 4394–4440, 4531–4548 |
| `upNextContainer` | 10 | 4 | 4083–4102, 4128–4154, 5437–5447, 5473 |
| `backdropImage` | 9 | 4 | 2250–2277, 2304–2308, 5402, 5501 |
| `emby-tab-button` | 9 | 4 | 525, 581, 3279, 5201–5237 |
| `sectionTabs` | 9 | 4 | 1541, 3279, 5085–5090, 5216–5242 |
| `button-link` | 7 | 4 | 525, 552, 2637–2646, 2707–2717 |
| `detailRibbon` | 7 | 4 | 1416–1444, 1577, 1652–1657, 6008 |
| `listItemBodyText` | 7 | 4 | 3525–3544, 3586, 3645, 5952 |
| `visualCardBox` | 7 | 4 | 379, 671–684, 710–715, 839 |
| `detailPagePrimaryContent` | 6 | 4 | 1431–1449, 2088, 3936, 5676 |
| `paper-icon-button-light` | 6 | 4 | 484–525, 1513, 1572, 4307 |
| `skip-button` | 6 | 4 | 525, 3284, 4177–4194, 4221–4227 |
| `button-submit` | 5 | 4 | 3300, 3387, 4806–4814, 5983 |
| `mainDrawer` | 5 | 4 | 2651, 5437–5447, 5718, 5757 |
| `sectionTitle` | 5 | 4 | 1517, 1551–1558, 4001, 4773 |
| `skinHeader-blurred` | 5 | 4 | 4720, 5073–5080, 5660, 5917 |
| `js` | 4 | 4 | 282, 1954, 2501, 5848 |
| `page` | 4 | 4 | 835, 2325, 2365, 5493 |
| `raised` | 4 | 4 | 525, 591, 3167, 3202 |
| `skinHeader-withBackground` | 4 | 4 | 1459, 4720, 5044, 5094 |
| `detailImageContainer` | 19 | 3 | 1733–1743, 1807–1882, 2123–2178 |
| `detailButton` | 12 | 3 | 484–525, 3212–3273, 3329–3333 |
| `emby-scroller` | 9 | 3 | 1522–1536, 5763–5810, 5903–5912 |
| `check` | 8 | 3 | 3003, 3221, 3637–3657 |
| `itemSelectionPanel` | 8 | 3 | 723–727, 2975, 3003–3040 |
| `pageTitle` | 8 | 3 | 1468–1504, 5105, 5164 |
| `detailSectionContent` | 6 | 3 | 2834, 3762–3772, 3838–3848 |
| `emby-checkbox` | 6 | 3 | 2980, 3017–3021, 3063–3075 |
| `headerTop` | 6 | 3 | 5055–5080, 5131–5148, 5175–5179 |
| `squareCard` | 6 | 3 | 694, 2136–2169, 4782–4786 |
| `actionSheetContent` | 5 | 3 | 3629–3633, 5437–5447, 5473 |
| `cardText-first` | 5 | 3 | 753, 3009–3035, 4887 |
| `dialog` | 5 | 3 | 2884–2894, 5437–5447, 5473 |
| `guideProgramName` | 5 | 3 | 525, 4572–4583, 4626–4631 |
| `musicParentName` | 5 | 3 | 1733, 2173–2178, 4513–4522 |
| `overflowBackdropCard` | 5 | 3 | 792–798, 3013, 4882–4887 |
| `cardPadder` | 4 | 3 | 375, 839, 3026–3030 |
| `cardText` | 4 | 3 | 753–763, 3035, 5836 |
| `cardText-secondary` | 4 | 3 | 753, 3035, 5572–5580 |
| `dialog-fullscreen` | 4 | 3 | 2894, 5437–5447, 5473 |
| `emby-scrollbuttons` | 4 | 3 | 1563–1568, 5848, 6160 |
| `infoWrapper` | 4 | 3 | 1846–1851, 2088, 2116 |
| `listItemImage` | 4 | 3 | 2420–2425, 3498, 5952 |
| `semiTransparent` | 4 | 3 | 1459, 4720, 5073–5094 |
| `toast` | 4 | 3 | 4075, 5437–5447, 5473 |
| `appfooter` | 3 | 3 | 2386, 5509, 5917 |
| `defaultCardBackground` | 3 | 3 | 3142, 4902, 5001 |
| `folder` | 3 | 3 | 1652, 3129, 3185 |
| `formDialogFooterItem` | 3 | 3 | 2955, 3180, 3306 |
| `itemsContainer` | 3 | 3 | 612, 1545, 3942 |
| `live_tv` | 3 | 3 | 1733, 2158, 3422 |
| `myPreferencesMenuPage` | 3 | 3 | 348, 3671, 3950 |
| `sectionTitle-cards` | 3 | 3 | 1517, 4001, 4051 |
| `x` | 3 | 3 | 1954, 4496, 5627 |
| `itemExternalLinks` | 11 | 2 | 2700–2757, 2834 |
| `mdl-slider` | 9 | 2 | 2497, 2552–2610 |
| `itemBackdrop` | 8 | 2 | 1699–1743, 2178 |
| `listItemIcon` | 8 | 2 | 3418–3422, 3641–3671 |
| `sectionTitleTextButton` | 8 | 2 | 3984–4021, 4055–4065 |
| `sliderContainer` | 8 | 2 | 2501, 2529–2594 |
| `detail-clamp-text` | 7 | 2 | 2770–2796, 2822–2826 |
| `backgroundContainer` | 6 | 2 | 2240, 2282–2300 |
| `detailPagePrimaryContainer` | 6 | 2 | 1403–1449, 2088 |
| `detailsGroupItem` | 6 | 2 | 3724, 3792–3816 |
| `divUsers` | 6 | 2 | 4782–4786, 5820–5840 |
| `headerLeft` | 6 | 2 | 1474–1504, 5330 |
| `trackSelections` | 6 | 2 | 3697–3724, 3843–3848 |
| `withBackdrop` | 6 | 2 | 2240, 2282–2300 |
| `detailSection` | 5 | 2 | 3680–3689, 3828–3848 |
| `headerButton` | 5 | 2 | 470–525, 5157 |
| `itemDetailsGroup` | 5 | 2 | 3776–3788, 3824–3848 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2660, 5731–5748 |
| `mediaInfoItem` | 5 | 2 | 1581–1624, 5627 |
| `overview-expand` | 5 | 2 | 2802–2826, 3762 |
| `playedIndicator` | 5 | 2 | 3112, 5692–5713 |
| `videoIndicator` | 5 | 2 | 3118–3138, 5974 |
| `withSectionTabs` | 5 | 2 | 2291–2308, 5080 |
| `album` | 4 | 2 | 1882, 2141–2158 |
| `emby-tab-button-active` | 4 | 2 | 3366, 5228–5242 |
| `noHomeButtonHeader` | 4 | 2 | 5105, 5201–5209 |
| `play_arrow` | 4 | 2 | 3147–3163, 3333 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3525–3530, 4995–5001 |
| `programCell` | 4 | 2 | 4563, 4622–4631 |
| `secondary` | 4 | 2 | 3534–3544, 3586 |
| `section0` | 4 | 2 | 805–835, 5493 |
| `visualLoginForm` | 4 | 2 | 4773–4790, 4831 |
| `alphaPickerButton` | 3 | 2 | 525, 3887–3894 |
| `cardFooter` | 3 | 2 | 3040, 5566–5585 |
| `castCollapsible` | 3 | 2 | 662, 3021–3030 |
| `detailPageContent` | 3 | 2 | 3693, 3929–3936 |
| `emby-scrollbuttons-button` | 3 | 2 | 1572, 6167–6174 |
| `guestCastContent` | 3 | 2 | 662, 3021–3030 |
| `guide-channelHeaderCell` | 3 | 2 | 525, 4597–4613 |
| `guide-date-tab-button` | 3 | 2 | 525, 3366–3374 |
| `manualLoginForm` | 3 | 2 | 4773–4790, 4831 |
| `overview` | 3 | 2 | 2822–2826, 3772 |
| `programGuideSection` | 3 | 2 | 2149, 3848–3863 |
| `selectionCommandsPanel` | 3 | 2 | 2965–2971, 5917 |
| `blurhash-canvas` | 2 | 2 | 5539, 5960 |
| `book` | 2 | 2 | 1733, 2158 |
| `btnDeleteImage` | 2 | 2 | 3167, 3380 |
| `cardContent` | 2 | 2 | 662, 694 |
| `cardImage` | 2 | 2 | 5539, 5960 |
| `cardOverlayButton-hover` | 2 | 2 | 748, 868 |
| `cardOverlayButtonIcon` | 2 | 2 | 851, 906 |
| `chevron_right` | 2 | 2 | 4021, 4065 |
| `collapseContent` | 2 | 2 | 2960, 3392 |
| `content-primary` | 2 | 2 | 3929, 3967 |
| `countIndicator` | 2 | 2 | 631, 5520 |
| `detailPageSecondaryContainer` | 2 | 2 | 1426, 1453 |
| `editorsChoiceItemOverview` | 2 | 2 | 6097, 6178 |
| `endsAt` | 2 | 2 | 1602, 5627 |
| `formDialogFooter` | 2 | 2 | 2955, 3392 |
| `formDialogFooter-clear` | 2 | 2 | 2955, 3392 |
| `formDialogHeader` | 2 | 2 | 3392, 5917 |
| `headerUserButton` | 2 | 2 | 470, 3954 |
| `headroom` | 2 | 2 | 5068, 5105 |
| `iconOsd` | 2 | 2 | 4698, 5917 |
| `mediaSourceIndicator` | 2 | 2 | 631, 5974 |
| `navMenuOption-selected` | 2 | 2 | 3676, 5742 |
| `nowPlayingInfoContainer` | 2 | 2 | 2691, 4932 |
| `org` | 2 | 2 | 2727, 2757 |
| `paperList` | 2 | 2 | 671, 3399 |
| `playlist` | 2 | 2 | 3520, 4910 |
| `queue` | 2 | 2 | 1733, 2158 |
| `readOnlyContent` | 2 | 2 | 3430, 5259 |
| `recordingFields` | 2 | 2 | 3716, 3843 |
| `runtime` | 2 | 2 | 4843, 4872 |
| `sectionTitleContainer` | 2 | 2 | 1568, 3872 |
| `sectionTitleContainer-cards` | 2 | 2 | 3996, 4051 |
| `tagline` | 2 | 2 | 2231, 3772 |
| `upNextDialog-title` | 2 | 2 | 4107, 4141 |
| `vertical-list` | 2 | 2 | 1545, 6003 |
| `videoOsdBottom` | 2 | 2 | 2683, 5035 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2683, 5035 |
| `checkboxOutline` | 10 | 1 | 2980–3075 |
| `cardOverlayButton-br` | 7 | 1 | 851–906 |
| `checkboxContainer` | 6 | 1 | 3009–3040 |
| `multiSelectCheckboxOutline` | 6 | 1 | 3017–3063 |
| `trackSelectionFieldContainer` | 6 | 1 | 3735–3758 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6134–6174 |
| `innerCardFooter` | 5 | 1 | 2847–2876 |
| `itemProgressBar` | 5 | 1 | 2420–2443 |
| `backgroundProgress` | 4 | 1 | 2431–2454 |
| `chapterCardImageContainer` | 4 | 1 | 2847–2876 |
| `endTimeText` | 4 | 1 | 4843–4872 |
| `mainDetailButtons` | 4 | 1 | 3329–3343 |
| `overview-controls` | 4 | 1 | 2822–2834 |
| `playbackProgress` | 4 | 1 | 2431–2459 |
| `scrollX` | 4 | 1 | 1522–1541 |
| `startTimeText` | 4 | 1 | 4843–4866 |
| `button-flat` | 3 | 1 | 2664–2674 |
| `cardIndicators` | 3 | 1 | 3092–3102 |
| `cardOverlayFab-primary` | 3 | 1 | 843–863 |
| `com` | 3 | 1 | 2733–2751 |
| `discover-card` | 3 | 1 | 6185–6208 |
| `emby-select-withcolor` | 3 | 1 | 4321–4355 |
| `emby-textarea` | 3 | 1 | 4312–4337 |
| `fab` | 3 | 1 | 3189–3202 |
| `listChildrenCollapsible` | 3 | 1 | 3833–3848 |
| `mdl-slider-background-flex` | 3 | 1 | 2521–2534 |
| `nextUpSection` | 3 | 1 | 3828–3848 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 4896–4906 |
| `serverInfo` | 3 | 1 | 3403–3412 |
| `transcodingProgress` | 3 | 1 | 2431–2443 |
