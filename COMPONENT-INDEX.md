# Index des composants — ElegantFin Cinema Edition v1.3.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.3.css` — 6640 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5687, 5974–5990, 6070–6092, 6122–6129, 6203, 6518 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3235, 3346, 3425, 4976, 5701–5711, 5780, 5974, 6113–6129 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5085–5089, 5170, 5693, 5772–5780, 5833, 5974–5990, 6113, 6251 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3192, 3351, 3425–3431, 3537, 3794, 4279, 4313–4323 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3888, 4165, 6346–6384 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4652–4704, 6346–6384 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5089, 5711, 5861–5880, 5974, 6258 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4658–4704, 4777, 6346–6384 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4712–4745, 6346–6384 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5687, 5974, 6258 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3504, 4988–5003, 5042, 5070–5089, 5716, 5759, 6102–6129 |
| `skinHeader` | 11 | 7 | 4984, 5313, 5369–5377, 5403–5428, 5763, 5942, 6455 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 2994–3001, 3371, 3406, 3559, 3812 |
| `js` | 7 | 7 | 286, 1566, 2120, 2693, 3325, 5889, 6139 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4165, 5772, 5889, 6139 |
| `paper-icon-button-light` | 9 | 6 | 537–592, 1580, 1650, 1709, 4184, 4571 |
| `nowPlayingBar` | 8 | 6 | 2879, 5222, 5726, 5820, 5923–5954, 6208 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3632, 6341 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3714–3740, 3771–3803, 6226–6243 |
| `osdHeader` | 15 | 5 | 1623–1641, 5308–5377, 5403–5428, 5763, 6208 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3714–3725, 3771, 3849–3865, 5744 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3781–3803, 3869–3874, 6013–6024 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3219, 5170 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5772, 5889 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3435–3477, 3510–3537 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6208–6226 |
| `itemName` | 11 | 4 | 649, 2120, 4658–4704, 4795–4812 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5680, 5780–5788 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3483, 5479–5515 |
| `upNextContainer` | 10 | 4 | 4341–4360, 4386–4412, 5716–5726, 5752 |
| `sectionTabs` | 9 | 4 | 1678, 3483, 5349–5354, 5494–5520 |
| `button-link` | 8 | 4 | 592, 619–637, 2829–2838, 2899–2909 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6341 |
| `listItemBodyText` | 7 | 4 | 3735–3754, 3794, 3853, 6243 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4159, 5958 |
| `skip-button` | 6 | 4 | 592, 3488, 4435–4452, 4479–4485 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5046–5050 |
| `button-submit` | 5 | 4 | 3504, 3591, 5070–5078, 6316 |
| `mainDrawer` | 5 | 4 | 2843, 5716–5726, 6000, 6039 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4259, 5037 |
| `skinHeader-blurred` | 5 | 4 | 4984, 5337–5344, 5942, 6208 |
| `appfooter` | 4 | 4 | 2578, 5453, 5803, 6208 |
| `page` | 4 | 4 | 926, 2512, 2557, 5772 |
| `raised` | 4 | 4 | 592, 678, 3371, 3406 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4984, 5308, 5358 |
| `detailButton` | 13 | 3 | 537–592, 3416–3477, 3533–3537 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6045–6092, 6194–6203 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3164, 3192–3235 |
| `check` | 8 | 3 | 3192, 3425, 3845–3865 |
| `pageTitle` | 8 | 3 | 1598–1641, 5369, 5428 |
| `detailSectionContent` | 6 | 3 | 3026, 3970–3980, 4061–4071 |
| `emby-checkbox` | 6 | 3 | 3169, 3206–3210, 3259–3271 |
| `headerTop` | 6 | 3 | 5319–5344, 5395–5412, 5439–5443 |
| `actionSheetContent` | 5 | 3 | 3837–3841, 5716–5726, 5752 |
| `cardText-first` | 5 | 3 | 844, 3198–3224, 5151 |
| `cardText-secondary` | 5 | 3 | 844, 3224–3228, 5867–5875 |
| `dialog` | 5 | 3 | 3076–3086, 5716–5726, 5752 |
| `guideProgramName` | 5 | 3 | 592, 4836–4847, 4890–4895 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4777–4786 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5369, 5479–5487 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3202, 5146–5151 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3215–3219 |
| `cardText` | 4 | 3 | 844–854, 3224, 6118 |
| `countIndicator` | 4 | 3 | 722, 5814, 6265–6289 |
| `dialog-fullscreen` | 4 | 3 | 3086, 5716–5726, 5752 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6139, 6493 |
| `formDialogFooter` | 4 | 3 | 3144, 3598, 6265–6289 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3708, 6243 |
| `semiTransparent` | 4 | 3 | 1562, 4984, 5337–5358 |
| `toast` | 4 | 3 | 4333, 5716–5726, 5752 |
| `defaultCardBackground` | 3 | 3 | 3346, 5166, 5265 |
| `folder` | 3 | 3 | 1799, 3325, 3389 |
| `formDialogFooterItem` | 3 | 3 | 3144, 3384, 3510 |
| `formDialogHeader` | 3 | 3 | 3598, 6208, 6265 |
| `iconOsd` | 3 | 3 | 4962, 6208, 6265 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4165 |
| `live_tv` | 3 | 3 | 1880, 2347, 3632 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3879, 4173 |
| `playerStats` | 3 | 3 | 4962, 6265, 6301 |
| `scss` | 3 | 3 | 956, 3241, 5889 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4259, 4309 |
| `x` | 3 | 3 | 2120, 4760, 5889 |
| `itemExternalLinks` | 11 | 2 | 2892–2949, 3026 |
| `checkboxOutline` | 10 | 2 | 3169–3210, 3241–3271 |
| `mdl-slider` | 9 | 2 | 2689, 2744–2802 |
| `listItemIcon` | 8 | 2 | 3628–3632, 3849–3879 |
| `sectionTitleTextButton` | 8 | 2 | 4242–4279, 4313–4323 |
| `sliderContainer` | 8 | 2 | 2693, 2721–2786 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2962–2988, 3014–3018 |
| `divUsers` | 7 | 2 | 5046–5050, 6102–6129 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3206–3210, 3240–3259 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3932, 4000–4038 |
| `headerButton` | 6 | 2 | 512–592, 5421 |
| `headerLeft` | 6 | 2 | 1604–1641, 5608 |
| `trackSelections` | 6 | 2 | 3905–3932, 4066–4071 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3888–3897, 4051–4071 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2852, 6013–6030 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5889 |
| `overview-expand` | 5 | 2 | 2994–3018, 3970 |
| `playedIndicator` | 5 | 2 | 3308, 5974–5995 |
| `videoIndicator` | 5 | 2 | 3314–3342, 6265 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5344 |
| `emby-tab-button-active` | 4 | 2 | 3570, 5506–5520 |
| `headerUserButton` | 4 | 2 | 512–525, 4177–4184 |
| `play_arrow` | 4 | 2 | 3351–3367, 3537 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3735–3740, 5259–5265 |
| `programCell` | 4 | 2 | 4827, 4886–4895 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4071–4086 |
| `secondary` | 4 | 2 | 3744–3754, 3794 |
| `section0` | 4 | 2 | 896–926, 5772 |
| `visualLoginForm` | 4 | 2 | 5037–5054, 5095 |
| `alphaPickerButton` | 3 | 2 | 592, 4110–4117 |
| `cardFooter` | 3 | 2 | 3235, 5861–5880 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3210–3219 |
| `detailPageContent` | 3 | 2 | 3901, 4152–4159 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6500–6507 |
| `fullSyncIndicator` | 3 | 2 | 722, 6265–6289 |
| `guestCastContent` | 3 | 2 | 753, 3210–3219 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4861–4877 |
| `guide-date-tab-button` | 3 | 2 | 592, 3570–3578 |
| `manualLoginForm` | 3 | 2 | 5037–5054, 5095 |
| `overview` | 3 | 2 | 3014–3018, 3980 |
| `selectionCommandsPanel` | 3 | 2 | 3154–3160, 6208 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6305 |
| `blurhash-canvas` | 2 | 2 | 5833, 6251 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3371, 3584 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5833, 6251 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4279, 4323 |
| `collapseContent` | 2 | 2 | 3149, 3596 |
| `content-primary` | 2 | 2 | 4152, 4225 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6430, 6511 |
| `endsAt` | 2 | 2 | 1739, 5889 |
| `formDialogFooter-clear` | 2 | 2 | 3144, 3598 |
| `headroom` | 2 | 2 | 5332, 5369 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5889 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6265 |
| `navMenuOption-selected` | 2 | 2 | 3884, 6024 |
| `nowPlayingInfoContainer` | 2 | 2 | 2883, 5196 |
| `org` | 2 | 2 | 2919, 2949 |
| `paperList` | 2 | 2 | 762, 3609 |
| `playlist` | 2 | 2 | 3730, 5174 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3640, 5537 |
| `recordingFields` | 2 | 2 | 3924, 4066 |
| `runtime` | 2 | 2 | 5107, 5136 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4095 |
| `sectionTitleContainer-cards` | 2 | 2 | 4254, 4309 |
| `tagline` | 2 | 2 | 2418, 3980 |
| `upNextDialog-title` | 2 | 2 | 4365, 4399 |
| `vertical-list` | 2 | 2 | 1682, 6336 |
| `videoOsdBottom` | 2 | 2 | 2875, 5299 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2875, 5299 |
| `checkboxContainer` | 7 | 1 | 3198–3235 |
| `itemDetailsGroup` | 7 | 1 | 3984–4071 |
| `trackSelectionFieldContainer` | 6 | 1 | 3943–3966 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6467–6507 |
| `innerCardFooter` | 5 | 1 | 3039–3068 |
| `itemProgressBar` | 5 | 1 | 2612–2635 |
| `backgroundProgress` | 4 | 1 | 2623–2646 |
| `chapterCardImageContainer` | 4 | 1 | 3039–3068 |
| `endTimeText` | 4 | 1 | 5107–5136 |
| `mainDetailButtons` | 4 | 1 | 3533–3547 |
| `overview-controls` | 4 | 1 | 3014–3026 |
| `playbackProgress` | 4 | 1 | 2623–2651 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5107–5130 |
| `button-flat` | 3 | 1 | 2856–2866 |
| `cardIndicators` | 3 | 1 | 3288–3298 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2925–2943 |
| `content` | 3 | 1 | 4007–4038 |
| `discover-card` | 3 | 1 | 6518–6541 |
| `emby-select-withcolor` | 3 | 1 | 4585–4619 |
| `emby-textarea` | 3 | 1 | 4576–4601 |
| `fab` | 3 | 1 | 3393–3406 |
| `listChildrenCollapsible` | 3 | 1 | 4056–4071 |
| `mdl-slider-background-flex` | 3 | 1 | 2713–2726 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4051–4071 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5160–5170 |
| `serverInfo` | 3 | 1 | 3613–3622 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
