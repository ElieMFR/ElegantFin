# Index des composants — ElegantFin Cinema Edition v1.3.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.3.css` — 6622 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5669, 5956–5972, 6052–6074, 6104–6111, 6185, 6500 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3235, 3346, 3425, 4958, 5683–5693, 5762, 5956, 6095–6111 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5067–5071, 5152, 5675, 5754–5762, 5815, 5956–5972, 6095, 6233 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3192, 3351, 3425–3431, 3537, 3794, 4261, 4295–4305 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3888, 4165, 6328–6366 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4634–4686, 6328–6366 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5071, 5693, 5843–5862, 5956, 6240 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4640–4686, 4759, 6328–6366 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4694–4727, 6328–6366 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5669, 5956, 6240 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3504, 4970–4985, 5024, 5052–5071, 5698, 5741, 6084–6111 |
| `skinHeader` | 11 | 7 | 4966, 5295, 5351–5359, 5385–5410, 5745, 5924, 6437 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 2994–3001, 3371, 3406, 3559, 3812 |
| `js` | 7 | 7 | 286, 1566, 2120, 2693, 3325, 5871, 6121 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4165, 5754, 5871, 6121 |
| `nowPlayingBar` | 8 | 6 | 2879, 5204, 5708, 5802, 5905–5936, 6190 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3632, 6323 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3714–3740, 3771–3803, 6208–6225 |
| `osdHeader` | 15 | 5 | 1623–1641, 5290–5359, 5385–5410, 5745, 6190 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3714–3725, 3771, 3849–3865, 5726 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3781–3803, 3869–3874, 5995–6006 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3219, 5152 |
| `paper-icon-button-light` | 8 | 5 | 537–592, 1580, 1650, 1709, 4553 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5754, 5871 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3435–3477, 3510–3537 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6190–6208 |
| `itemName` | 11 | 4 | 649, 2120, 4640–4686, 4777–4794 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5662, 5762–5770 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3483, 5461–5497 |
| `upNextContainer` | 10 | 4 | 4323–4342, 4368–4394, 5698–5708, 5734 |
| `sectionTabs` | 9 | 4 | 1678, 3483, 5331–5336, 5476–5502 |
| `button-link` | 8 | 4 | 592, 619–637, 2829–2838, 2899–2909 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6323 |
| `listItemBodyText` | 7 | 4 | 3735–3754, 3794, 3853, 6225 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4159, 5940 |
| `skip-button` | 6 | 4 | 592, 3488, 4417–4434, 4461–4467 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5028–5032 |
| `button-submit` | 5 | 4 | 3504, 3591, 5052–5060, 6298 |
| `mainDrawer` | 5 | 4 | 2843, 5698–5708, 5982, 6021 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4241, 5019 |
| `skinHeader-blurred` | 5 | 4 | 4966, 5319–5326, 5924, 6190 |
| `appfooter` | 4 | 4 | 2578, 5435, 5785, 6190 |
| `page` | 4 | 4 | 926, 2512, 2557, 5754 |
| `raised` | 4 | 4 | 592, 678, 3371, 3406 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4966, 5290, 5340 |
| `detailButton` | 13 | 3 | 537–592, 3416–3477, 3533–3537 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6027–6074, 6176–6185 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3164, 3192–3235 |
| `check` | 8 | 3 | 3192, 3425, 3845–3865 |
| `pageTitle` | 8 | 3 | 1598–1641, 5351, 5410 |
| `detailSectionContent` | 6 | 3 | 3026, 3970–3980, 4061–4071 |
| `emby-checkbox` | 6 | 3 | 3169, 3206–3210, 3259–3271 |
| `headerTop` | 6 | 3 | 5301–5326, 5377–5394, 5421–5425 |
| `actionSheetContent` | 5 | 3 | 3837–3841, 5698–5708, 5734 |
| `cardText-first` | 5 | 3 | 844, 3198–3224, 5133 |
| `cardText-secondary` | 5 | 3 | 844, 3224–3228, 5849–5857 |
| `dialog` | 5 | 3 | 3076–3086, 5698–5708, 5734 |
| `guideProgramName` | 5 | 3 | 592, 4818–4829, 4872–4877 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4759–4768 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5351, 5461–5469 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3202, 5128–5133 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3215–3219 |
| `cardText` | 4 | 3 | 844–854, 3224, 6100 |
| `countIndicator` | 4 | 3 | 722, 5796, 6247–6271 |
| `dialog-fullscreen` | 4 | 3 | 3086, 5698–5708, 5734 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6121, 6475 |
| `formDialogFooter` | 4 | 3 | 3144, 3598, 6247–6271 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3708, 6225 |
| `semiTransparent` | 4 | 3 | 1562, 4966, 5319–5340 |
| `toast` | 4 | 3 | 4315, 5698–5708, 5734 |
| `defaultCardBackground` | 3 | 3 | 3346, 5148, 5247 |
| `folder` | 3 | 3 | 1799, 3325, 3389 |
| `formDialogFooterItem` | 3 | 3 | 3144, 3384, 3510 |
| `formDialogHeader` | 3 | 3 | 3598, 6190, 6247 |
| `iconOsd` | 3 | 3 | 4944, 6190, 6247 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4165 |
| `live_tv` | 3 | 3 | 1880, 2347, 3632 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3879, 4173 |
| `playerStats` | 3 | 3 | 4944, 6247, 6283 |
| `scss` | 3 | 3 | 956, 3241, 5871 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4241, 4291 |
| `x` | 3 | 3 | 2120, 4742, 5871 |
| `itemExternalLinks` | 11 | 2 | 2892–2949, 3026 |
| `checkboxOutline` | 10 | 2 | 3169–3210, 3241–3271 |
| `mdl-slider` | 9 | 2 | 2689, 2744–2802 |
| `listItemIcon` | 8 | 2 | 3628–3632, 3849–3879 |
| `sectionTitleTextButton` | 8 | 2 | 4224–4261, 4295–4305 |
| `sliderContainer` | 8 | 2 | 2693, 2721–2786 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2962–2988, 3014–3018 |
| `divUsers` | 7 | 2 | 5028–5032, 6084–6111 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3206–3210, 3240–3259 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3932, 4000–4038 |
| `headerButton` | 6 | 2 | 512–592, 5403 |
| `headerLeft` | 6 | 2 | 1604–1641, 5590 |
| `trackSelections` | 6 | 2 | 3905–3932, 4066–4071 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3888–3897, 4051–4071 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2852, 5995–6012 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5871 |
| `overview-expand` | 5 | 2 | 2994–3018, 3970 |
| `playedIndicator` | 5 | 2 | 3308, 5956–5977 |
| `videoIndicator` | 5 | 2 | 3314–3342, 6247 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5326 |
| `emby-tab-button-active` | 4 | 2 | 3570, 5488–5502 |
| `headerUserButton` | 4 | 2 | 512–525, 4177–4184 |
| `play_arrow` | 4 | 2 | 3351–3367, 3537 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3735–3740, 5241–5247 |
| `programCell` | 4 | 2 | 4809, 4868–4877 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4071–4086 |
| `secondary` | 4 | 2 | 3744–3754, 3794 |
| `section0` | 4 | 2 | 896–926, 5754 |
| `visualLoginForm` | 4 | 2 | 5019–5036, 5077 |
| `alphaPickerButton` | 3 | 2 | 592, 4110–4117 |
| `cardFooter` | 3 | 2 | 3235, 5843–5862 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3210–3219 |
| `detailPageContent` | 3 | 2 | 3901, 4152–4159 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6482–6489 |
| `fullSyncIndicator` | 3 | 2 | 722, 6247–6271 |
| `guestCastContent` | 3 | 2 | 753, 3210–3219 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4843–4859 |
| `guide-date-tab-button` | 3 | 2 | 592, 3570–3578 |
| `manualLoginForm` | 3 | 2 | 5019–5036, 5077 |
| `overview` | 3 | 2 | 3014–3018, 3980 |
| `selectionCommandsPanel` | 3 | 2 | 3154–3160, 6190 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6287 |
| `blurhash-canvas` | 2 | 2 | 5815, 6233 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3371, 3584 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5815, 6233 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4261, 4305 |
| `collapseContent` | 2 | 2 | 3149, 3596 |
| `content-primary` | 2 | 2 | 4152, 4207 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6412, 6493 |
| `endsAt` | 2 | 2 | 1739, 5871 |
| `formDialogFooter-clear` | 2 | 2 | 3144, 3598 |
| `headroom` | 2 | 2 | 5314, 5351 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5871 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6247 |
| `navMenuOption-selected` | 2 | 2 | 3884, 6006 |
| `nowPlayingInfoContainer` | 2 | 2 | 2883, 5178 |
| `org` | 2 | 2 | 2919, 2949 |
| `paperList` | 2 | 2 | 762, 3609 |
| `playlist` | 2 | 2 | 3730, 5156 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3640, 5519 |
| `recordingFields` | 2 | 2 | 3924, 4066 |
| `runtime` | 2 | 2 | 5089, 5118 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4095 |
| `sectionTitleContainer-cards` | 2 | 2 | 4236, 4291 |
| `tagline` | 2 | 2 | 2418, 3980 |
| `upNextDialog-title` | 2 | 2 | 4347, 4381 |
| `vertical-list` | 2 | 2 | 1682, 6318 |
| `videoOsdBottom` | 2 | 2 | 2875, 5281 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2875, 5281 |
| `checkboxContainer` | 7 | 1 | 3198–3235 |
| `itemDetailsGroup` | 7 | 1 | 3984–4071 |
| `trackSelectionFieldContainer` | 6 | 1 | 3943–3966 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6449–6489 |
| `innerCardFooter` | 5 | 1 | 3039–3068 |
| `itemProgressBar` | 5 | 1 | 2612–2635 |
| `backgroundProgress` | 4 | 1 | 2623–2646 |
| `chapterCardImageContainer` | 4 | 1 | 3039–3068 |
| `endTimeText` | 4 | 1 | 5089–5118 |
| `mainDetailButtons` | 4 | 1 | 3533–3547 |
| `overview-controls` | 4 | 1 | 3014–3026 |
| `playbackProgress` | 4 | 1 | 2623–2651 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5089–5112 |
| `button-flat` | 3 | 1 | 2856–2866 |
| `cardIndicators` | 3 | 1 | 3288–3298 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2925–2943 |
| `content` | 3 | 1 | 4007–4038 |
| `discover-card` | 3 | 1 | 6500–6523 |
| `emby-select-withcolor` | 3 | 1 | 4567–4601 |
| `emby-textarea` | 3 | 1 | 4558–4583 |
| `fab` | 3 | 1 | 3393–3406 |
| `listChildrenCollapsible` | 3 | 1 | 4056–4071 |
| `mdl-slider-background-flex` | 3 | 1 | 2713–2726 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4051–4071 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5142–5152 |
| `serverInfo` | 3 | 1 | 3613–3622 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
