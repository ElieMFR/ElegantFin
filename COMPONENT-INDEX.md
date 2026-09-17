# Index des composants — ElegantFin Cinema Edition v1.3.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.3.css` — 6642 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5689, 5976–5992, 6072–6094, 6124–6131, 6205, 6520 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3235, 3346, 3425, 4978, 5703–5713, 5782, 5976, 6115–6131 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5087–5091, 5172, 5695, 5774–5782, 5835, 5976–5992, 6115, 6253 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3192, 3351, 3425–3431, 3537, 3794, 4281, 4315–4325 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3888, 4165, 6348–6386 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4654–4706, 6348–6386 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5091, 5713, 5863–5882, 5976, 6260 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4660–4706, 4779, 6348–6386 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4714–4747, 6348–6386 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5689, 5976, 6260 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3504, 4990–5005, 5044, 5072–5091, 5718, 5761, 6104–6131 |
| `skinHeader` | 11 | 7 | 4986, 5315, 5371–5379, 5405–5430, 5765, 5944, 6457 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 2994–3001, 3371, 3406, 3559, 3812 |
| `js` | 7 | 7 | 286, 1566, 2120, 2693, 3325, 5891, 6141 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4165, 5774, 5891, 6141 |
| `paper-icon-button-light` | 9 | 6 | 537–592, 1580, 1650, 1709, 4191, 4573 |
| `nowPlayingBar` | 8 | 6 | 2879, 5224, 5728, 5822, 5925–5956, 6210 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3632, 6343 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3714–3740, 3771–3803, 6228–6245 |
| `osdHeader` | 15 | 5 | 1623–1641, 5310–5379, 5405–5430, 5765, 6210 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3714–3725, 3771, 3849–3865, 5746 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3781–3803, 3869–3874, 6015–6026 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3219, 5172 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5774, 5891 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3435–3477, 3510–3537 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6210–6228 |
| `itemName` | 11 | 4 | 649, 2120, 4660–4706, 4797–4814 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5682, 5782–5790 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3483, 5481–5517 |
| `upNextContainer` | 10 | 4 | 4343–4362, 4388–4414, 5718–5728, 5754 |
| `sectionTabs` | 9 | 4 | 1678, 3483, 5351–5356, 5496–5522 |
| `button-link` | 8 | 4 | 592, 619–637, 2829–2838, 2899–2909 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6343 |
| `listItemBodyText` | 7 | 4 | 3735–3754, 3794, 3853, 6245 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4159, 5960 |
| `skip-button` | 6 | 4 | 592, 3488, 4437–4454, 4481–4487 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5048–5052 |
| `button-submit` | 5 | 4 | 3504, 3591, 5072–5080, 6318 |
| `mainDrawer` | 5 | 4 | 2843, 5718–5728, 6002, 6041 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4261, 5039 |
| `skinHeader-blurred` | 5 | 4 | 4986, 5339–5346, 5944, 6210 |
| `appfooter` | 4 | 4 | 2578, 5455, 5805, 6210 |
| `page` | 4 | 4 | 926, 2512, 2557, 5774 |
| `raised` | 4 | 4 | 592, 678, 3371, 3406 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4986, 5310, 5360 |
| `detailButton` | 13 | 3 | 537–592, 3416–3477, 3533–3537 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6047–6094, 6196–6205 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3164, 3192–3235 |
| `check` | 8 | 3 | 3192, 3425, 3845–3865 |
| `pageTitle` | 8 | 3 | 1598–1641, 5371, 5430 |
| `detailSectionContent` | 6 | 3 | 3026, 3970–3980, 4061–4071 |
| `emby-checkbox` | 6 | 3 | 3169, 3206–3210, 3259–3271 |
| `headerTop` | 6 | 3 | 5321–5346, 5397–5414, 5441–5445 |
| `actionSheetContent` | 5 | 3 | 3837–3841, 5718–5728, 5754 |
| `cardText-first` | 5 | 3 | 844, 3198–3224, 5153 |
| `cardText-secondary` | 5 | 3 | 844, 3224–3228, 5869–5877 |
| `dialog` | 5 | 3 | 3076–3086, 5718–5728, 5754 |
| `guideProgramName` | 5 | 3 | 592, 4838–4849, 4892–4897 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4779–4788 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5371, 5481–5489 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3202, 5148–5153 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3215–3219 |
| `cardText` | 4 | 3 | 844–854, 3224, 6120 |
| `countIndicator` | 4 | 3 | 722, 5816, 6267–6291 |
| `dialog-fullscreen` | 4 | 3 | 3086, 5718–5728, 5754 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6141, 6495 |
| `formDialogFooter` | 4 | 3 | 3144, 3598, 6267–6291 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3708, 6245 |
| `semiTransparent` | 4 | 3 | 1562, 4986, 5339–5360 |
| `toast` | 4 | 3 | 4335, 5718–5728, 5754 |
| `defaultCardBackground` | 3 | 3 | 3346, 5168, 5267 |
| `folder` | 3 | 3 | 1799, 3325, 3389 |
| `formDialogFooterItem` | 3 | 3 | 3144, 3384, 3510 |
| `formDialogHeader` | 3 | 3 | 3598, 6210, 6267 |
| `iconOsd` | 3 | 3 | 4964, 6210, 6267 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4165 |
| `live_tv` | 3 | 3 | 1880, 2347, 3632 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3879, 4173 |
| `playerStats` | 3 | 3 | 4964, 6267, 6303 |
| `scss` | 3 | 3 | 956, 3241, 5891 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4261, 4311 |
| `x` | 3 | 3 | 2120, 4762, 5891 |
| `itemExternalLinks` | 11 | 2 | 2892–2949, 3026 |
| `checkboxOutline` | 10 | 2 | 3169–3210, 3241–3271 |
| `mdl-slider` | 9 | 2 | 2689, 2744–2802 |
| `listItemIcon` | 8 | 2 | 3628–3632, 3849–3879 |
| `sectionTitleTextButton` | 8 | 2 | 4244–4281, 4315–4325 |
| `sliderContainer` | 8 | 2 | 2693, 2721–2786 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2962–2988, 3014–3018 |
| `divUsers` | 7 | 2 | 5048–5052, 6104–6131 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3206–3210, 3240–3259 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3932, 4000–4038 |
| `headerButton` | 6 | 2 | 512–592, 5423 |
| `headerLeft` | 6 | 2 | 1604–1641, 5610 |
| `trackSelections` | 6 | 2 | 3905–3932, 4066–4071 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3888–3897, 4051–4071 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2852, 6015–6032 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5891 |
| `overview-expand` | 5 | 2 | 2994–3018, 3970 |
| `playedIndicator` | 5 | 2 | 3308, 5976–5997 |
| `videoIndicator` | 5 | 2 | 3314–3342, 6267 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5346 |
| `emby-tab-button-active` | 4 | 2 | 3570, 5508–5522 |
| `headerUserButton` | 4 | 2 | 512–525, 4177–4191 |
| `play_arrow` | 4 | 2 | 3351–3367, 3537 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3735–3740, 5261–5267 |
| `programCell` | 4 | 2 | 4829, 4888–4897 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4071–4086 |
| `secondary` | 4 | 2 | 3744–3754, 3794 |
| `section0` | 4 | 2 | 896–926, 5774 |
| `visualLoginForm` | 4 | 2 | 5039–5056, 5097 |
| `alphaPickerButton` | 3 | 2 | 592, 4110–4117 |
| `cardFooter` | 3 | 2 | 3235, 5863–5882 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3210–3219 |
| `detailPageContent` | 3 | 2 | 3901, 4152–4159 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6502–6509 |
| `fullSyncIndicator` | 3 | 2 | 722, 6267–6291 |
| `guestCastContent` | 3 | 2 | 753, 3210–3219 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4863–4879 |
| `guide-date-tab-button` | 3 | 2 | 592, 3570–3578 |
| `manualLoginForm` | 3 | 2 | 5039–5056, 5097 |
| `overview` | 3 | 2 | 3014–3018, 3980 |
| `selectionCommandsPanel` | 3 | 2 | 3154–3160, 6210 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6307 |
| `blurhash-canvas` | 2 | 2 | 5835, 6253 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3371, 3584 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5835, 6253 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4281, 4325 |
| `collapseContent` | 2 | 2 | 3149, 3596 |
| `content-primary` | 2 | 2 | 4152, 4227 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6432, 6513 |
| `endsAt` | 2 | 2 | 1739, 5891 |
| `formDialogFooter-clear` | 2 | 2 | 3144, 3598 |
| `headroom` | 2 | 2 | 5334, 5371 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5891 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6267 |
| `navMenuOption-selected` | 2 | 2 | 3884, 6026 |
| `nowPlayingInfoContainer` | 2 | 2 | 2883, 5198 |
| `org` | 2 | 2 | 2919, 2949 |
| `paperList` | 2 | 2 | 762, 3609 |
| `playlist` | 2 | 2 | 3730, 5176 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3640, 5539 |
| `recordingFields` | 2 | 2 | 3924, 4066 |
| `runtime` | 2 | 2 | 5109, 5138 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4095 |
| `sectionTitleContainer-cards` | 2 | 2 | 4256, 4311 |
| `tagline` | 2 | 2 | 2418, 3980 |
| `upNextDialog-title` | 2 | 2 | 4367, 4401 |
| `vertical-list` | 2 | 2 | 1682, 6338 |
| `videoOsdBottom` | 2 | 2 | 2875, 5301 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2875, 5301 |
| `checkboxContainer` | 7 | 1 | 3198–3235 |
| `itemDetailsGroup` | 7 | 1 | 3984–4071 |
| `trackSelectionFieldContainer` | 6 | 1 | 3943–3966 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6469–6509 |
| `innerCardFooter` | 5 | 1 | 3039–3068 |
| `itemProgressBar` | 5 | 1 | 2612–2635 |
| `backgroundProgress` | 4 | 1 | 2623–2646 |
| `chapterCardImageContainer` | 4 | 1 | 3039–3068 |
| `endTimeText` | 4 | 1 | 5109–5138 |
| `mainDetailButtons` | 4 | 1 | 3533–3547 |
| `overview-controls` | 4 | 1 | 3014–3026 |
| `playbackProgress` | 4 | 1 | 2623–2651 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5109–5132 |
| `button-flat` | 3 | 1 | 2856–2866 |
| `cardIndicators` | 3 | 1 | 3288–3298 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2925–2943 |
| `content` | 3 | 1 | 4007–4038 |
| `discover-card` | 3 | 1 | 6520–6543 |
| `emby-select-withcolor` | 3 | 1 | 4587–4621 |
| `emby-textarea` | 3 | 1 | 4578–4603 |
| `fab` | 3 | 1 | 3393–3406 |
| `listChildrenCollapsible` | 3 | 1 | 4056–4071 |
| `mdl-slider-background-flex` | 3 | 1 | 2713–2726 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4051–4071 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5162–5172 |
| `serverInfo` | 3 | 1 | 3613–3622 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
