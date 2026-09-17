# Index des composants — ElegantFin Cinema Edition v1.3.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.3.css` — 6619 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5666, 5953–5969, 6049–6071, 6101–6108, 6182, 6497 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3235, 3346, 3425, 4955, 5680–5690, 5759, 5953, 6092–6108 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5064–5068, 5149, 5672, 5751–5759, 5812, 5953–5969, 6092, 6230 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3192, 3351, 3425–3431, 3537, 3794, 4258, 4292–4302 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3888, 4165, 6325–6363 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4631–4683, 6325–6363 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5068, 5690, 5840–5859, 5953, 6237 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4637–4683, 4756, 6325–6363 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4691–4724, 6325–6363 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5666, 5953, 6237 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3504, 4967–4982, 5021, 5049–5068, 5695, 5738, 6081–6108 |
| `skinHeader` | 11 | 7 | 4963, 5292, 5348–5356, 5382–5407, 5742, 5921, 6434 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 2994–3001, 3371, 3406, 3559, 3812 |
| `js` | 7 | 7 | 286, 1566, 2120, 2693, 3325, 5868, 6118 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4165, 5751, 5868, 6118 |
| `nowPlayingBar` | 8 | 6 | 2879, 5201, 5705, 5799, 5902–5933, 6187 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3632, 6320 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3714–3740, 3771–3803, 6205–6222 |
| `osdHeader` | 15 | 5 | 1623–1641, 5287–5356, 5382–5407, 5742, 6187 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3714–3725, 3771, 3849–3865, 5723 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3781–3803, 3869–3874, 5992–6003 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3219, 5149 |
| `paper-icon-button-light` | 8 | 5 | 537–592, 1580, 1650, 1709, 4550 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5751, 5868 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3435–3477, 3510–3537 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6187–6205 |
| `itemName` | 11 | 4 | 649, 2120, 4637–4683, 4774–4791 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5659, 5759–5767 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3483, 5458–5494 |
| `upNextContainer` | 10 | 4 | 4320–4339, 4365–4391, 5695–5705, 5731 |
| `sectionTabs` | 9 | 4 | 1678, 3483, 5328–5333, 5473–5499 |
| `button-link` | 8 | 4 | 592, 619–637, 2829–2838, 2899–2909 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6320 |
| `listItemBodyText` | 7 | 4 | 3735–3754, 3794, 3853, 6222 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4159, 5937 |
| `skip-button` | 6 | 4 | 592, 3488, 4414–4431, 4458–4464 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5025–5029 |
| `button-submit` | 5 | 4 | 3504, 3591, 5049–5057, 6295 |
| `mainDrawer` | 5 | 4 | 2843, 5695–5705, 5979, 6018 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4238, 5016 |
| `skinHeader-blurred` | 5 | 4 | 4963, 5316–5323, 5921, 6187 |
| `appfooter` | 4 | 4 | 2578, 5432, 5782, 6187 |
| `page` | 4 | 4 | 926, 2512, 2557, 5751 |
| `raised` | 4 | 4 | 592, 678, 3371, 3406 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4963, 5287, 5337 |
| `detailButton` | 13 | 3 | 537–592, 3416–3477, 3533–3537 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6024–6071, 6173–6182 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3164, 3192–3235 |
| `check` | 8 | 3 | 3192, 3425, 3845–3865 |
| `pageTitle` | 8 | 3 | 1598–1641, 5348, 5407 |
| `detailSectionContent` | 6 | 3 | 3026, 3970–3980, 4061–4071 |
| `emby-checkbox` | 6 | 3 | 3169, 3206–3210, 3259–3271 |
| `headerTop` | 6 | 3 | 5298–5323, 5374–5391, 5418–5422 |
| `actionSheetContent` | 5 | 3 | 3837–3841, 5695–5705, 5731 |
| `cardText-first` | 5 | 3 | 844, 3198–3224, 5130 |
| `cardText-secondary` | 5 | 3 | 844, 3224–3228, 5846–5854 |
| `dialog` | 5 | 3 | 3076–3086, 5695–5705, 5731 |
| `guideProgramName` | 5 | 3 | 592, 4815–4826, 4869–4874 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4756–4765 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5348, 5458–5466 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3202, 5125–5130 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3215–3219 |
| `cardText` | 4 | 3 | 844–854, 3224, 6097 |
| `countIndicator` | 4 | 3 | 722, 5793, 6244–6268 |
| `dialog-fullscreen` | 4 | 3 | 3086, 5695–5705, 5731 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6118, 6472 |
| `formDialogFooter` | 4 | 3 | 3144, 3598, 6244–6268 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3708, 6222 |
| `semiTransparent` | 4 | 3 | 1562, 4963, 5316–5337 |
| `toast` | 4 | 3 | 4312, 5695–5705, 5731 |
| `defaultCardBackground` | 3 | 3 | 3346, 5145, 5244 |
| `folder` | 3 | 3 | 1799, 3325, 3389 |
| `formDialogFooterItem` | 3 | 3 | 3144, 3384, 3510 |
| `formDialogHeader` | 3 | 3 | 3598, 6187, 6244 |
| `iconOsd` | 3 | 3 | 4941, 6187, 6244 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4165 |
| `live_tv` | 3 | 3 | 1880, 2347, 3632 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3879, 4173 |
| `playerStats` | 3 | 3 | 4941, 6244, 6280 |
| `scss` | 3 | 3 | 956, 3241, 5868 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4238, 4288 |
| `x` | 3 | 3 | 2120, 4739, 5868 |
| `itemExternalLinks` | 11 | 2 | 2892–2949, 3026 |
| `checkboxOutline` | 10 | 2 | 3169–3210, 3241–3271 |
| `mdl-slider` | 9 | 2 | 2689, 2744–2802 |
| `listItemIcon` | 8 | 2 | 3628–3632, 3849–3879 |
| `sectionTitleTextButton` | 8 | 2 | 4221–4258, 4292–4302 |
| `sliderContainer` | 8 | 2 | 2693, 2721–2786 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2962–2988, 3014–3018 |
| `divUsers` | 7 | 2 | 5025–5029, 6081–6108 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3206–3210, 3240–3259 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3932, 4000–4038 |
| `headerButton` | 6 | 2 | 512–592, 5400 |
| `headerLeft` | 6 | 2 | 1604–1641, 5587 |
| `trackSelections` | 6 | 2 | 3905–3932, 4066–4071 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3888–3897, 4051–4071 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2852, 5992–6009 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5868 |
| `overview-expand` | 5 | 2 | 2994–3018, 3970 |
| `playedIndicator` | 5 | 2 | 3308, 5953–5974 |
| `videoIndicator` | 5 | 2 | 3314–3342, 6244 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5323 |
| `emby-tab-button-active` | 4 | 2 | 3570, 5485–5499 |
| `play_arrow` | 4 | 2 | 3351–3367, 3537 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3735–3740, 5238–5244 |
| `programCell` | 4 | 2 | 4806, 4865–4874 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4071–4086 |
| `secondary` | 4 | 2 | 3744–3754, 3794 |
| `section0` | 4 | 2 | 896–926, 5751 |
| `visualLoginForm` | 4 | 2 | 5016–5033, 5074 |
| `alphaPickerButton` | 3 | 2 | 592, 4110–4117 |
| `cardFooter` | 3 | 2 | 3235, 5840–5859 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3210–3219 |
| `detailPageContent` | 3 | 2 | 3901, 4152–4159 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6479–6486 |
| `fullSyncIndicator` | 3 | 2 | 722, 6244–6268 |
| `guestCastContent` | 3 | 2 | 753, 3210–3219 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4840–4856 |
| `guide-date-tab-button` | 3 | 2 | 592, 3570–3578 |
| `headerUserButton` | 3 | 2 | 512–525, 4177 |
| `manualLoginForm` | 3 | 2 | 5016–5033, 5074 |
| `overview` | 3 | 2 | 3014–3018, 3980 |
| `selectionCommandsPanel` | 3 | 2 | 3154–3160, 6187 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6284 |
| `blurhash-canvas` | 2 | 2 | 5812, 6230 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3371, 3584 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5812, 6230 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4258, 4302 |
| `collapseContent` | 2 | 2 | 3149, 3596 |
| `content-primary` | 2 | 2 | 4152, 4204 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6409, 6490 |
| `endsAt` | 2 | 2 | 1739, 5868 |
| `formDialogFooter-clear` | 2 | 2 | 3144, 3598 |
| `headroom` | 2 | 2 | 5311, 5348 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5868 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6244 |
| `navMenuOption-selected` | 2 | 2 | 3884, 6003 |
| `nowPlayingInfoContainer` | 2 | 2 | 2883, 5175 |
| `org` | 2 | 2 | 2919, 2949 |
| `paperList` | 2 | 2 | 762, 3609 |
| `playlist` | 2 | 2 | 3730, 5153 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3640, 5516 |
| `recordingFields` | 2 | 2 | 3924, 4066 |
| `runtime` | 2 | 2 | 5086, 5115 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4095 |
| `sectionTitleContainer-cards` | 2 | 2 | 4233, 4288 |
| `tagline` | 2 | 2 | 2418, 3980 |
| `upNextDialog-title` | 2 | 2 | 4344, 4378 |
| `vertical-list` | 2 | 2 | 1682, 6315 |
| `videoOsdBottom` | 2 | 2 | 2875, 5278 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2875, 5278 |
| `checkboxContainer` | 7 | 1 | 3198–3235 |
| `itemDetailsGroup` | 7 | 1 | 3984–4071 |
| `trackSelectionFieldContainer` | 6 | 1 | 3943–3966 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6446–6486 |
| `innerCardFooter` | 5 | 1 | 3039–3068 |
| `itemProgressBar` | 5 | 1 | 2612–2635 |
| `backgroundProgress` | 4 | 1 | 2623–2646 |
| `chapterCardImageContainer` | 4 | 1 | 3039–3068 |
| `endTimeText` | 4 | 1 | 5086–5115 |
| `mainDetailButtons` | 4 | 1 | 3533–3547 |
| `overview-controls` | 4 | 1 | 3014–3026 |
| `playbackProgress` | 4 | 1 | 2623–2651 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5086–5109 |
| `button-flat` | 3 | 1 | 2856–2866 |
| `cardIndicators` | 3 | 1 | 3288–3298 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2925–2943 |
| `content` | 3 | 1 | 4007–4038 |
| `discover-card` | 3 | 1 | 6497–6520 |
| `emby-select-withcolor` | 3 | 1 | 4564–4598 |
| `emby-textarea` | 3 | 1 | 4555–4580 |
| `fab` | 3 | 1 | 3393–3406 |
| `listChildrenCollapsible` | 3 | 1 | 4056–4071 |
| `mdl-slider-background-flex` | 3 | 1 | 2713–2726 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4051–4071 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5139–5149 |
| `serverInfo` | 3 | 1 | 3613–3622 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
