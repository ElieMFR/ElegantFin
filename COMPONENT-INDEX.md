# Index des composants — ElegantFin Cinema Edition v1.3.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.3.css` — 6610 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5657, 5944–5960, 6040–6062, 6092–6099, 6173, 6488 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3235, 3346, 3425, 4946, 5671–5681, 5750, 5944, 6083–6099 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5055–5059, 5140, 5663, 5742–5750, 5803, 5944–5960, 6083, 6221 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3192, 3351, 3425–3431, 3537, 3794, 4249, 4283–4293 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3888, 4165, 6316–6354 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4622–4674, 6316–6354 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5059, 5681, 5831–5850, 5944, 6228 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4628–4674, 4747, 6316–6354 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4682–4715, 6316–6354 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5657, 5944, 6228 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3504, 4958–4973, 5012, 5040–5059, 5686, 5729, 6072–6099 |
| `skinHeader` | 11 | 7 | 4954, 5283, 5339–5347, 5373–5398, 5733, 5912, 6425 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 2994–3001, 3371, 3406, 3559, 3812 |
| `js` | 7 | 7 | 286, 1566, 2120, 2693, 3325, 5859, 6109 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4165, 5742, 5859, 6109 |
| `nowPlayingBar` | 8 | 6 | 2879, 5192, 5696, 5790, 5893–5924, 6178 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3632, 6311 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3714–3740, 3771–3803, 6196–6213 |
| `osdHeader` | 15 | 5 | 1623–1641, 5278–5347, 5373–5398, 5733, 6178 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3714–3725, 3771, 3849–3865, 5714 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3781–3803, 3869–3874, 5983–5994 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3219, 5140 |
| `paper-icon-button-light` | 8 | 5 | 537–592, 1580, 1650, 1709, 4541 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5742, 5859 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3435–3477, 3510–3537 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6178–6196 |
| `itemName` | 11 | 4 | 649, 2120, 4628–4674, 4765–4782 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5650, 5750–5758 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3483, 5449–5485 |
| `upNextContainer` | 10 | 4 | 4311–4330, 4356–4382, 5686–5696, 5722 |
| `sectionTabs` | 9 | 4 | 1678, 3483, 5319–5324, 5464–5490 |
| `button-link` | 8 | 4 | 592, 619–637, 2829–2838, 2899–2909 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6311 |
| `listItemBodyText` | 7 | 4 | 3735–3754, 3794, 3853, 6213 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4159, 5928 |
| `skip-button` | 6 | 4 | 592, 3488, 4405–4422, 4449–4455 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5016–5020 |
| `button-submit` | 5 | 4 | 3504, 3591, 5040–5048, 6286 |
| `mainDrawer` | 5 | 4 | 2843, 5686–5696, 5970, 6009 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4229, 5007 |
| `skinHeader-blurred` | 5 | 4 | 4954, 5307–5314, 5912, 6178 |
| `appfooter` | 4 | 4 | 2578, 5423, 5773, 6178 |
| `page` | 4 | 4 | 926, 2512, 2557, 5742 |
| `raised` | 4 | 4 | 592, 678, 3371, 3406 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4954, 5278, 5328 |
| `detailButton` | 13 | 3 | 537–592, 3416–3477, 3533–3537 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6015–6062, 6164–6173 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3164, 3192–3235 |
| `check` | 8 | 3 | 3192, 3425, 3845–3865 |
| `pageTitle` | 8 | 3 | 1598–1641, 5339, 5398 |
| `detailSectionContent` | 6 | 3 | 3026, 3970–3980, 4061–4071 |
| `emby-checkbox` | 6 | 3 | 3169, 3206–3210, 3259–3271 |
| `headerTop` | 6 | 3 | 5289–5314, 5365–5382, 5409–5413 |
| `actionSheetContent` | 5 | 3 | 3837–3841, 5686–5696, 5722 |
| `cardText-first` | 5 | 3 | 844, 3198–3224, 5121 |
| `cardText-secondary` | 5 | 3 | 844, 3224–3228, 5837–5845 |
| `dialog` | 5 | 3 | 3076–3086, 5686–5696, 5722 |
| `guideProgramName` | 5 | 3 | 592, 4806–4817, 4860–4865 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4747–4756 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5339, 5449–5457 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3202, 5116–5121 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3215–3219 |
| `cardText` | 4 | 3 | 844–854, 3224, 6088 |
| `countIndicator` | 4 | 3 | 722, 5784, 6235–6259 |
| `dialog-fullscreen` | 4 | 3 | 3086, 5686–5696, 5722 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6109, 6463 |
| `formDialogFooter` | 4 | 3 | 3144, 3598, 6235–6259 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3708, 6213 |
| `semiTransparent` | 4 | 3 | 1562, 4954, 5307–5328 |
| `toast` | 4 | 3 | 4303, 5686–5696, 5722 |
| `defaultCardBackground` | 3 | 3 | 3346, 5136, 5235 |
| `folder` | 3 | 3 | 1799, 3325, 3389 |
| `formDialogFooterItem` | 3 | 3 | 3144, 3384, 3510 |
| `formDialogHeader` | 3 | 3 | 3598, 6178, 6235 |
| `iconOsd` | 3 | 3 | 4932, 6178, 6235 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4165 |
| `live_tv` | 3 | 3 | 1880, 2347, 3632 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3879, 4173 |
| `playerStats` | 3 | 3 | 4932, 6235, 6271 |
| `scss` | 3 | 3 | 956, 3241, 5859 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4229, 4279 |
| `x` | 3 | 3 | 2120, 4730, 5859 |
| `itemExternalLinks` | 11 | 2 | 2892–2949, 3026 |
| `checkboxOutline` | 10 | 2 | 3169–3210, 3241–3271 |
| `mdl-slider` | 9 | 2 | 2689, 2744–2802 |
| `listItemIcon` | 8 | 2 | 3628–3632, 3849–3879 |
| `sectionTitleTextButton` | 8 | 2 | 4212–4249, 4283–4293 |
| `sliderContainer` | 8 | 2 | 2693, 2721–2786 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2962–2988, 3014–3018 |
| `divUsers` | 7 | 2 | 5016–5020, 6072–6099 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3206–3210, 3240–3259 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3932, 4000–4038 |
| `headerButton` | 6 | 2 | 512–592, 5391 |
| `headerLeft` | 6 | 2 | 1604–1641, 5578 |
| `trackSelections` | 6 | 2 | 3905–3932, 4066–4071 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3888–3897, 4051–4071 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2852, 5983–6000 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5859 |
| `overview-expand` | 5 | 2 | 2994–3018, 3970 |
| `playedIndicator` | 5 | 2 | 3308, 5944–5965 |
| `videoIndicator` | 5 | 2 | 3314–3342, 6235 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5314 |
| `emby-tab-button-active` | 4 | 2 | 3570, 5476–5490 |
| `play_arrow` | 4 | 2 | 3351–3367, 3537 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3735–3740, 5229–5235 |
| `programCell` | 4 | 2 | 4797, 4856–4865 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4071–4086 |
| `secondary` | 4 | 2 | 3744–3754, 3794 |
| `section0` | 4 | 2 | 896–926, 5742 |
| `visualLoginForm` | 4 | 2 | 5007–5024, 5065 |
| `alphaPickerButton` | 3 | 2 | 592, 4110–4117 |
| `cardFooter` | 3 | 2 | 3235, 5831–5850 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3210–3219 |
| `detailPageContent` | 3 | 2 | 3901, 4152–4159 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6470–6477 |
| `fullSyncIndicator` | 3 | 2 | 722, 6235–6259 |
| `guestCastContent` | 3 | 2 | 753, 3210–3219 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4831–4847 |
| `guide-date-tab-button` | 3 | 2 | 592, 3570–3578 |
| `headerUserButton` | 3 | 2 | 512–525, 4177 |
| `manualLoginForm` | 3 | 2 | 5007–5024, 5065 |
| `overview` | 3 | 2 | 3014–3018, 3980 |
| `selectionCommandsPanel` | 3 | 2 | 3154–3160, 6178 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6275 |
| `blurhash-canvas` | 2 | 2 | 5803, 6221 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3371, 3584 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5803, 6221 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4249, 4293 |
| `collapseContent` | 2 | 2 | 3149, 3596 |
| `content-primary` | 2 | 2 | 4152, 4195 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6400, 6481 |
| `endsAt` | 2 | 2 | 1739, 5859 |
| `formDialogFooter-clear` | 2 | 2 | 3144, 3598 |
| `headroom` | 2 | 2 | 5302, 5339 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5859 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6235 |
| `navMenuOption-selected` | 2 | 2 | 3884, 5994 |
| `nowPlayingInfoContainer` | 2 | 2 | 2883, 5166 |
| `org` | 2 | 2 | 2919, 2949 |
| `paperList` | 2 | 2 | 762, 3609 |
| `playlist` | 2 | 2 | 3730, 5144 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3640, 5507 |
| `recordingFields` | 2 | 2 | 3924, 4066 |
| `runtime` | 2 | 2 | 5077, 5106 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4095 |
| `sectionTitleContainer-cards` | 2 | 2 | 4224, 4279 |
| `tagline` | 2 | 2 | 2418, 3980 |
| `upNextDialog-title` | 2 | 2 | 4335, 4369 |
| `vertical-list` | 2 | 2 | 1682, 6306 |
| `videoOsdBottom` | 2 | 2 | 2875, 5269 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2875, 5269 |
| `checkboxContainer` | 7 | 1 | 3198–3235 |
| `itemDetailsGroup` | 7 | 1 | 3984–4071 |
| `trackSelectionFieldContainer` | 6 | 1 | 3943–3966 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6437–6477 |
| `innerCardFooter` | 5 | 1 | 3039–3068 |
| `itemProgressBar` | 5 | 1 | 2612–2635 |
| `backgroundProgress` | 4 | 1 | 2623–2646 |
| `chapterCardImageContainer` | 4 | 1 | 3039–3068 |
| `endTimeText` | 4 | 1 | 5077–5106 |
| `mainDetailButtons` | 4 | 1 | 3533–3547 |
| `overview-controls` | 4 | 1 | 3014–3026 |
| `playbackProgress` | 4 | 1 | 2623–2651 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5077–5100 |
| `button-flat` | 3 | 1 | 2856–2866 |
| `cardIndicators` | 3 | 1 | 3288–3298 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2925–2943 |
| `content` | 3 | 1 | 4007–4038 |
| `discover-card` | 3 | 1 | 6488–6511 |
| `emby-select-withcolor` | 3 | 1 | 4555–4589 |
| `emby-textarea` | 3 | 1 | 4546–4571 |
| `fab` | 3 | 1 | 3393–3406 |
| `listChildrenCollapsible` | 3 | 1 | 4056–4071 |
| `mdl-slider-background-flex` | 3 | 1 | 2713–2726 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4051–4071 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5130–5140 |
| `serverInfo` | 3 | 1 | 3613–3622 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
