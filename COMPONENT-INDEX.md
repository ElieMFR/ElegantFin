# Index des composants — ElegantFin Cinema Edition v1.3.4

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.4.css` — 6654 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5701, 5988–6004, 6084–6106, 6136–6143, 6217, 6532 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3254, 3365, 3444, 4990, 5715–5725, 5794, 5988, 6127–6143 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5099–5103, 5184, 5707, 5786–5794, 5847, 5988–6004, 6127, 6265 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3211, 3370, 3444–3450, 3556, 3813, 4277, 4311–4321 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3907, 4184, 6360–6398 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4650–4702, 6360–6398 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5103, 5725, 5875–5894, 5988, 6272 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4656–4702, 4775, 6360–6398 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4710–4743, 6360–6398 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5701, 5988, 6272 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3523, 5002–5017, 5056, 5084–5103, 5730, 5773, 6116–6143 |
| `skinHeader` | 11 | 7 | 4998, 5327, 5383–5391, 5417–5442, 5777, 5956, 6469 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 3013–3020, 3390, 3425, 3578, 3831 |
| `js` | 7 | 7 | 286, 1566, 2120, 2712, 3344, 5903, 6153 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4184, 5786, 5903, 6153 |
| `nowPlayingBar` | 8 | 6 | 2898, 5236, 5740, 5834, 5937–5968, 6222 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3651, 6355 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3733–3759, 3790–3822, 6240–6257 |
| `osdHeader` | 15 | 5 | 1623–1641, 5322–5391, 5417–5442, 5777, 6222 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3733–3744, 3790, 3868–3884, 5758 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3800–3822, 3888–3893, 6027–6038 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3238, 5184 |
| `paper-icon-button-light` | 8 | 5 | 537–592, 1580, 1650, 1709, 4569 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5786, 5903 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3454–3496, 3529–3556 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6222–6240 |
| `itemName` | 11 | 4 | 649, 2120, 4656–4702, 4793–4810 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5694, 5794–5802 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3502, 5493–5529 |
| `upNextContainer` | 10 | 4 | 4339–4358, 4384–4410, 5730–5740, 5766 |
| `sectionTabs` | 9 | 4 | 1678, 3502, 5363–5368, 5508–5534 |
| `button-link` | 8 | 4 | 592, 619–637, 2848–2857, 2918–2928 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6355 |
| `listItemBodyText` | 7 | 4 | 3754–3773, 3813, 3872, 6257 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4178, 5972 |
| `skip-button` | 6 | 4 | 592, 3507, 4433–4450, 4477–4483 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5060–5064 |
| `button-submit` | 5 | 4 | 3523, 3610, 5084–5092, 6330 |
| `mainDrawer` | 5 | 4 | 2862, 5730–5740, 6014, 6053 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4257, 5051 |
| `skinHeader-blurred` | 5 | 4 | 4998, 5351–5358, 5956, 6222 |
| `appfooter` | 4 | 4 | 2578, 5467, 5817, 6222 |
| `page` | 4 | 4 | 926, 2512, 2557, 5786 |
| `raised` | 4 | 4 | 592, 678, 3390, 3425 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4998, 5322, 5372 |
| `detailButton` | 13 | 3 | 537–592, 3435–3496, 3552–3556 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6059–6106, 6208–6217 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3183, 3211–3254 |
| `check` | 8 | 3 | 3211, 3444, 3864–3884 |
| `pageTitle` | 8 | 3 | 1598–1641, 5383, 5442 |
| `detailSectionContent` | 6 | 3 | 3045, 3989–3999, 4080–4090 |
| `emby-checkbox` | 6 | 3 | 3188, 3225–3229, 3278–3290 |
| `headerTop` | 6 | 3 | 5333–5358, 5409–5426, 5453–5457 |
| `actionSheetContent` | 5 | 3 | 3856–3860, 5730–5740, 5766 |
| `cardText-first` | 5 | 3 | 844, 3217–3243, 5165 |
| `cardText-secondary` | 5 | 3 | 844, 3243–3247, 5881–5889 |
| `dialog` | 5 | 3 | 3095–3105, 5730–5740, 5766 |
| `guideProgramName` | 5 | 3 | 592, 4834–4845, 4888–4893 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4775–4784 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5383, 5493–5501 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3221, 5160–5165 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3234–3238 |
| `cardText` | 4 | 3 | 844–854, 3243, 6132 |
| `countIndicator` | 4 | 3 | 722, 5828, 6279–6303 |
| `dialog-fullscreen` | 4 | 3 | 3105, 5730–5740, 5766 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6153, 6507 |
| `formDialogFooter` | 4 | 3 | 3163, 3617, 6279–6303 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3727, 6257 |
| `semiTransparent` | 4 | 3 | 1562, 4998, 5351–5372 |
| `toast` | 4 | 3 | 4331, 5730–5740, 5766 |
| `defaultCardBackground` | 3 | 3 | 3365, 5180, 5279 |
| `folder` | 3 | 3 | 1799, 3344, 3408 |
| `formDialogFooterItem` | 3 | 3 | 3163, 3403, 3529 |
| `formDialogHeader` | 3 | 3 | 3617, 6222, 6279 |
| `iconOsd` | 3 | 3 | 4976, 6222, 6279 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4184 |
| `live_tv` | 3 | 3 | 1880, 2347, 3651 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3898, 4192 |
| `playerStats` | 3 | 3 | 4976, 6279, 6315 |
| `scss` | 3 | 3 | 956, 3260, 5903 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4257, 4307 |
| `x` | 3 | 3 | 2120, 4758, 5903 |
| `itemExternalLinks` | 11 | 2 | 2911–2968, 3045 |
| `checkboxOutline` | 10 | 2 | 3188–3229, 3260–3290 |
| `mdl-slider` | 9 | 2 | 2708, 2763–2821 |
| `listItemIcon` | 8 | 2 | 3647–3651, 3868–3898 |
| `sectionTitleTextButton` | 8 | 2 | 4240–4277, 4311–4321 |
| `sliderContainer` | 8 | 2 | 2712, 2740–2805 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2981–3007, 3033–3037 |
| `divUsers` | 7 | 2 | 5060–5064, 6116–6143 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3225–3229, 3259–3278 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3951, 4019–4057 |
| `headerButton` | 6 | 2 | 512–592, 5435 |
| `headerLeft` | 6 | 2 | 1604–1641, 5622 |
| `trackSelections` | 6 | 2 | 3924–3951, 4085–4090 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3907–3916, 4070–4090 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2871, 6027–6044 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5903 |
| `overview-expand` | 5 | 2 | 3013–3037, 3989 |
| `playedIndicator` | 5 | 2 | 3327, 5988–6009 |
| `videoIndicator` | 5 | 2 | 3333–3361, 6279 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5358 |
| `backgroundProgress` | 4 | 2 | 2623–2635, 2665 |
| `emby-tab-button-active` | 4 | 2 | 3589, 5520–5534 |
| `play_arrow` | 4 | 2 | 3370–3386, 3556 |
| `playbackProgress` | 4 | 2 | 2623–2635, 2670 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3754–3759, 5273–5279 |
| `programCell` | 4 | 2 | 4825, 4884–4893 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4090–4105 |
| `secondary` | 4 | 2 | 3763–3773, 3813 |
| `section0` | 4 | 2 | 896–926, 5786 |
| `visualLoginForm` | 4 | 2 | 5051–5068, 5109 |
| `alphaPickerButton` | 3 | 2 | 592, 4129–4136 |
| `cardFooter` | 3 | 2 | 3254, 5875–5894 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3229–3238 |
| `detailPageContent` | 3 | 2 | 3920, 4171–4178 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6514–6521 |
| `fullSyncIndicator` | 3 | 2 | 722, 6279–6303 |
| `guestCastContent` | 3 | 2 | 753, 3229–3238 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4859–4875 |
| `guide-date-tab-button` | 3 | 2 | 592, 3589–3597 |
| `headerUserButton` | 3 | 2 | 512–525, 4196 |
| `manualLoginForm` | 3 | 2 | 5051–5068, 5109 |
| `overview` | 3 | 2 | 3033–3037, 3999 |
| `selectionCommandsPanel` | 3 | 2 | 3173–3179, 6222 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6319 |
| `blurhash-canvas` | 2 | 2 | 5847, 6265 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3390, 3603 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5847, 6265 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4277, 4321 |
| `collapseContent` | 2 | 2 | 3168, 3615 |
| `content-primary` | 2 | 2 | 4171, 4223 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6444, 6525 |
| `endsAt` | 2 | 2 | 1739, 5903 |
| `formDialogFooter-clear` | 2 | 2 | 3163, 3617 |
| `headroom` | 2 | 2 | 5346, 5383 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5903 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6279 |
| `navMenuOption-selected` | 2 | 2 | 3903, 6038 |
| `nowPlayingInfoContainer` | 2 | 2 | 2902, 5210 |
| `org` | 2 | 2 | 2938, 2968 |
| `paperList` | 2 | 2 | 762, 3628 |
| `playlist` | 2 | 2 | 3749, 5188 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3659, 5551 |
| `recordingFields` | 2 | 2 | 3943, 4085 |
| `runtime` | 2 | 2 | 5121, 5150 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4114 |
| `sectionTitleContainer-cards` | 2 | 2 | 4252, 4307 |
| `tagline` | 2 | 2 | 2418, 3999 |
| `upNextDialog-title` | 2 | 2 | 4363, 4397 |
| `vertical-list` | 2 | 2 | 1682, 6350 |
| `videoOsdBottom` | 2 | 2 | 2894, 5313 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2894, 5313 |
| `checkboxContainer` | 7 | 1 | 3217–3254 |
| `itemDetailsGroup` | 7 | 1 | 4003–4090 |
| `itemProgressBar` | 6 | 1 | 2612–2646 |
| `trackSelectionFieldContainer` | 6 | 1 | 3962–3985 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6481–6521 |
| `innerCardFooter` | 5 | 1 | 3058–3087 |
| `chapterCardImageContainer` | 4 | 1 | 3058–3087 |
| `endTimeText` | 4 | 1 | 5121–5150 |
| `mainDetailButtons` | 4 | 1 | 3552–3566 |
| `overview-controls` | 4 | 1 | 3033–3045 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5121–5144 |
| `button-flat` | 3 | 1 | 2875–2885 |
| `cardIndicators` | 3 | 1 | 3307–3317 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2944–2962 |
| `content` | 3 | 1 | 4026–4057 |
| `discover-card` | 3 | 1 | 6532–6555 |
| `emby-select-withcolor` | 3 | 1 | 4583–4617 |
| `emby-textarea` | 3 | 1 | 4574–4599 |
| `fab` | 3 | 1 | 3412–3425 |
| `listChildrenCollapsible` | 3 | 1 | 4075–4090 |
| `mdl-slider-background-flex` | 3 | 1 | 2732–2745 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4070–4090 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5174–5184 |
| `serverInfo` | 3 | 1 | 3632–3641 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
