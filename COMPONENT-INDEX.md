# Index des composants — ElegantFin Cinema Edition v1.3.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.3.css` — 6592 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5652, 5939–5955, 6035–6057, 6087–6094, 6168, 6483 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3235, 3346, 3425, 4941, 5666–5676, 5745, 5939, 6078–6094 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5050–5054, 5135, 5658, 5737–5745, 5798, 5939–5955, 6078, 6216 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3192, 3351, 3425–3431, 3537, 3794, 4244, 4278–4288 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3888, 4165, 6311–6349 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4617–4669, 6311–6349 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5054, 5676, 5826–5845, 5939, 6223 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4623–4669, 4742, 6311–6349 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4677–4710, 6311–6349 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5652, 5939, 6223 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3504, 4953–4968, 5007, 5035–5054, 5681, 5724, 6067–6094 |
| `skinHeader` | 11 | 7 | 4949, 5278, 5334–5342, 5368–5393, 5728, 5907, 6420 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 2994–3001, 3371, 3406, 3559, 3812 |
| `js` | 7 | 7 | 286, 1566, 2120, 2693, 3325, 5854, 6104 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4165, 5737, 5854, 6104 |
| `nowPlayingBar` | 8 | 6 | 2879, 5187, 5691, 5785, 5888–5919, 6173 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3632, 6306 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3714–3740, 3771–3803, 6191–6208 |
| `osdHeader` | 15 | 5 | 1623–1641, 5273–5342, 5368–5393, 5728, 6173 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3714–3725, 3771, 3849–3865, 5709 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3781–3803, 3869–3874, 5978–5989 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3219, 5135 |
| `paper-icon-button-light` | 8 | 5 | 537–592, 1580, 1650, 1709, 4536 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5737, 5854 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3435–3477, 3510–3537 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6173–6191 |
| `itemName` | 11 | 4 | 649, 2120, 4623–4669, 4760–4777 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5645, 5745–5753 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3483, 5444–5480 |
| `upNextContainer` | 10 | 4 | 4306–4325, 4351–4377, 5681–5691, 5717 |
| `sectionTabs` | 9 | 4 | 1678, 3483, 5314–5319, 5459–5485 |
| `button-link` | 8 | 4 | 592, 619–637, 2829–2838, 2899–2909 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6306 |
| `listItemBodyText` | 7 | 4 | 3735–3754, 3794, 3853, 6208 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4159, 5923 |
| `skip-button` | 6 | 4 | 592, 3488, 4400–4417, 4444–4450 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5011–5015 |
| `button-submit` | 5 | 4 | 3504, 3591, 5035–5043, 6281 |
| `mainDrawer` | 5 | 4 | 2843, 5681–5691, 5965, 6004 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4224, 5002 |
| `skinHeader-blurred` | 5 | 4 | 4949, 5302–5309, 5907, 6173 |
| `appfooter` | 4 | 4 | 2578, 5418, 5768, 6173 |
| `page` | 4 | 4 | 926, 2512, 2557, 5737 |
| `raised` | 4 | 4 | 592, 678, 3371, 3406 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4949, 5273, 5323 |
| `detailButton` | 13 | 3 | 537–592, 3416–3477, 3533–3537 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6010–6057, 6159–6168 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3164, 3192–3235 |
| `check` | 8 | 3 | 3192, 3425, 3845–3865 |
| `pageTitle` | 8 | 3 | 1598–1641, 5334, 5393 |
| `detailSectionContent` | 6 | 3 | 3026, 3970–3980, 4061–4071 |
| `emby-checkbox` | 6 | 3 | 3169, 3206–3210, 3259–3271 |
| `headerTop` | 6 | 3 | 5284–5309, 5360–5377, 5404–5408 |
| `actionSheetContent` | 5 | 3 | 3837–3841, 5681–5691, 5717 |
| `cardText-first` | 5 | 3 | 844, 3198–3224, 5116 |
| `cardText-secondary` | 5 | 3 | 844, 3224–3228, 5832–5840 |
| `dialog` | 5 | 3 | 3076–3086, 5681–5691, 5717 |
| `guideProgramName` | 5 | 3 | 592, 4801–4812, 4855–4860 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4742–4751 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5334, 5444–5452 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3202, 5111–5116 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3215–3219 |
| `cardText` | 4 | 3 | 844–854, 3224, 6083 |
| `countIndicator` | 4 | 3 | 722, 5779, 6230–6254 |
| `dialog-fullscreen` | 4 | 3 | 3086, 5681–5691, 5717 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6104, 6458 |
| `formDialogFooter` | 4 | 3 | 3144, 3598, 6230–6254 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3708, 6208 |
| `semiTransparent` | 4 | 3 | 1562, 4949, 5302–5323 |
| `toast` | 4 | 3 | 4298, 5681–5691, 5717 |
| `defaultCardBackground` | 3 | 3 | 3346, 5131, 5230 |
| `folder` | 3 | 3 | 1799, 3325, 3389 |
| `formDialogFooterItem` | 3 | 3 | 3144, 3384, 3510 |
| `formDialogHeader` | 3 | 3 | 3598, 6173, 6230 |
| `iconOsd` | 3 | 3 | 4927, 6173, 6230 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4165 |
| `live_tv` | 3 | 3 | 1880, 2347, 3632 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3879, 4173 |
| `playerStats` | 3 | 3 | 4927, 6230, 6266 |
| `scss` | 3 | 3 | 956, 3241, 5854 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4224, 4274 |
| `x` | 3 | 3 | 2120, 4725, 5854 |
| `itemExternalLinks` | 11 | 2 | 2892–2949, 3026 |
| `checkboxOutline` | 10 | 2 | 3169–3210, 3241–3271 |
| `mdl-slider` | 9 | 2 | 2689, 2744–2802 |
| `listItemIcon` | 8 | 2 | 3628–3632, 3849–3879 |
| `sectionTitleTextButton` | 8 | 2 | 4207–4244, 4278–4288 |
| `sliderContainer` | 8 | 2 | 2693, 2721–2786 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2962–2988, 3014–3018 |
| `divUsers` | 7 | 2 | 5011–5015, 6067–6094 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3206–3210, 3240–3259 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3932, 4000–4038 |
| `headerButton` | 6 | 2 | 512–592, 5386 |
| `headerLeft` | 6 | 2 | 1604–1641, 5573 |
| `trackSelections` | 6 | 2 | 3905–3932, 4066–4071 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3888–3897, 4051–4071 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2852, 5978–5995 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5854 |
| `overview-expand` | 5 | 2 | 2994–3018, 3970 |
| `playedIndicator` | 5 | 2 | 3308, 5939–5960 |
| `videoIndicator` | 5 | 2 | 3314–3342, 6230 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5309 |
| `emby-tab-button-active` | 4 | 2 | 3570, 5471–5485 |
| `play_arrow` | 4 | 2 | 3351–3367, 3537 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3735–3740, 5224–5230 |
| `programCell` | 4 | 2 | 4792, 4851–4860 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4071–4086 |
| `secondary` | 4 | 2 | 3744–3754, 3794 |
| `section0` | 4 | 2 | 896–926, 5737 |
| `visualLoginForm` | 4 | 2 | 5002–5019, 5060 |
| `alphaPickerButton` | 3 | 2 | 592, 4110–4117 |
| `cardFooter` | 3 | 2 | 3235, 5826–5845 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3210–3219 |
| `detailPageContent` | 3 | 2 | 3901, 4152–4159 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6465–6472 |
| `fullSyncIndicator` | 3 | 2 | 722, 6230–6254 |
| `guestCastContent` | 3 | 2 | 753, 3210–3219 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4826–4842 |
| `guide-date-tab-button` | 3 | 2 | 592, 3570–3578 |
| `headerUserButton` | 3 | 2 | 512–525, 4177 |
| `manualLoginForm` | 3 | 2 | 5002–5019, 5060 |
| `overview` | 3 | 2 | 3014–3018, 3980 |
| `selectionCommandsPanel` | 3 | 2 | 3154–3160, 6173 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6270 |
| `blurhash-canvas` | 2 | 2 | 5798, 6216 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3371, 3584 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5798, 6216 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4244, 4288 |
| `collapseContent` | 2 | 2 | 3149, 3596 |
| `content-primary` | 2 | 2 | 4152, 4190 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6395, 6476 |
| `endsAt` | 2 | 2 | 1739, 5854 |
| `formDialogFooter-clear` | 2 | 2 | 3144, 3598 |
| `headroom` | 2 | 2 | 5297, 5334 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5854 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6230 |
| `navMenuOption-selected` | 2 | 2 | 3884, 5989 |
| `nowPlayingInfoContainer` | 2 | 2 | 2883, 5161 |
| `org` | 2 | 2 | 2919, 2949 |
| `paperList` | 2 | 2 | 762, 3609 |
| `playlist` | 2 | 2 | 3730, 5139 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3640, 5502 |
| `recordingFields` | 2 | 2 | 3924, 4066 |
| `runtime` | 2 | 2 | 5072, 5101 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4095 |
| `sectionTitleContainer-cards` | 2 | 2 | 4219, 4274 |
| `tagline` | 2 | 2 | 2418, 3980 |
| `upNextDialog-title` | 2 | 2 | 4330, 4364 |
| `vertical-list` | 2 | 2 | 1682, 6301 |
| `videoOsdBottom` | 2 | 2 | 2875, 5264 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2875, 5264 |
| `checkboxContainer` | 7 | 1 | 3198–3235 |
| `itemDetailsGroup` | 7 | 1 | 3984–4071 |
| `trackSelectionFieldContainer` | 6 | 1 | 3943–3966 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6432–6472 |
| `innerCardFooter` | 5 | 1 | 3039–3068 |
| `itemProgressBar` | 5 | 1 | 2612–2635 |
| `backgroundProgress` | 4 | 1 | 2623–2646 |
| `chapterCardImageContainer` | 4 | 1 | 3039–3068 |
| `endTimeText` | 4 | 1 | 5072–5101 |
| `mainDetailButtons` | 4 | 1 | 3533–3547 |
| `overview-controls` | 4 | 1 | 3014–3026 |
| `playbackProgress` | 4 | 1 | 2623–2651 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5072–5095 |
| `button-flat` | 3 | 1 | 2856–2866 |
| `cardIndicators` | 3 | 1 | 3288–3298 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2925–2943 |
| `content` | 3 | 1 | 4007–4038 |
| `discover-card` | 3 | 1 | 6483–6506 |
| `emby-select-withcolor` | 3 | 1 | 4550–4584 |
| `emby-textarea` | 3 | 1 | 4541–4566 |
| `fab` | 3 | 1 | 3393–3406 |
| `listChildrenCollapsible` | 3 | 1 | 4056–4071 |
| `mdl-slider-background-flex` | 3 | 1 | 2713–2726 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4051–4071 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5125–5135 |
| `serverInfo` | 3 | 1 | 3613–3622 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
