# Index des composants — ElegantFin Cinema Edition v1.3.1

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.1.css` — 6409 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 15 | 383–394, 426–438, 620, 702, 1348–1368, 1871–1904, 1931–1935, 2210–2228, 2264, 5557, 5844–5860, 5940–5962, 5992, 6064, 6379 |
| `cardScalable` | 25 | 13 | 383–394, 431–438, 648–692, 718–756, 2228, 3146, 3257, 3336, 4846, 5571–5581, 5650, 5844, 5983–5992 |
| `cardImageContainer` | 23 | 13 | 426, 670, 698–727, 756, 813–843, 4955–4959, 5040, 5563, 5642–5650, 5703, 5844–5860, 5983, 6112 |
| `material-icons` | 15 | 11 | 319–338, 1567, 1626, 1678, 3109, 3262, 3336–3342, 3448, 3705, 4155, 4189–4199 |
| `itemDetailPage` | 16 | 10 | 1411, 1497, 1576, 1797–1822, 1866, 1966, 2277–2282, 3799, 4076, 6207–6245 |
| `nameContainer` | 27 | 9 | 575, 1973–1996, 2037, 2066, 2101–2147, 2184, 2215–2219, 4522–4574, 6207–6245 |
| `backdropCard` | 12 | 9 | 800–806, 921, 1797, 1883, 1966, 2219–2228, 2255, 2282, 2552 |
| `card-hoverable` | 23 | 8 | 438, 658, 718–806, 4959, 5581, 5731–5750, 5844, 6119 |
| `parentName` | 23 | 8 | 575, 1978–1996, 2037, 2066, 2101–2147, 4528–4574, 4647, 6207–6245 |
| `detailPageWrapperContainer` | 17 | 8 | 575, 1379–1389, 1822, 1940, 1973–1996, 2066, 2101–2147, 2215 |
| `subtitle` | 16 | 8 | 1797, 1866, 1978, 2037, 2156–2166, 2277–2282, 4582–4615, 6207–6245 |
| `cardBox` | 11 | 8 | 383–394, 420–438, 620, 740, 847, 5557, 5844, 6119 |
| `detailLogo` | 17 | 7 | 575, 1811–1822, 1857–1866, 1966–1996, 2066, 2101–2147, 2215 |
| `loginPage` | 14 | 7 | 3415, 4858–4873, 4912, 4940–4959, 5586, 5629, 5972–5992 |
| `skinHeader` | 11 | 7 | 4854, 5183, 5239–5247, 5273–5298, 5633, 5812, 6316 |
| `emby-button` | 9 | 7 | 512–529, 556, 2911–2918, 3282, 3317, 3470, 3723 |
| `js` | 7 | 7 | 286, 1483, 2037, 2610, 3236, 5759, 6000 |
| `verticalSection` | 11 | 6 | 1571, 2448–2453, 4076, 5642, 5759, 6000 |
| `nowPlayingBar` | 8 | 6 | 2796, 5092, 5596, 5690, 5793–5824, 6069 |
| `person` | 8 | 6 | 1797–1807, 1966, 2219, 2264–2273, 3543, 6202 |
| `detailImageContainer` | 20 | 5 | 1797–1807, 1871–1935, 1966, 2206–2228, 2255–2282 |
| `listItem` | 16 | 5 | 529, 2232, 3625–3651, 3682–3714, 6087–6104 |
| `osdHeader` | 15 | 5 | 1540–1558, 5178–5247, 5273–5298, 5633, 6069 |
| `actionSheetMenuItem` | 11 | 5 | 529, 3625–3636, 3682, 3760–3776, 5614 |
| `navMenuOption` | 11 | 5 | 529, 605–615, 3692–3714, 3780–3785, 5883–5894 |
| `cardImageIcon` | 8 | 5 | 375–379, 2219–2228, 2288, 3136, 5040 |
| `emby-scroller-container` | 7 | 5 | 1571–1584, 2438, 2474, 5642, 5759 |
| `paper-icon-button-light` | 7 | 5 | 488–529, 1497, 1567, 1626, 4441 |
| `portraitCard` | 5 | 5 | 921, 999, 1716, 1931, 2552 |
| `btnPlay` | 14 | 4 | 449, 488–529, 3346–3388, 3421–3448 |
| `cardOverlayContainer` | 12 | 4 | 774–806, 851–873, 933, 6069–6087 |
| `itemName` | 11 | 4 | 575, 2037, 4528–4574, 4665–4682 |
| `backdropImage` | 10 | 4 | 2354–2381, 2408–2412, 5550, 5650–5658 |
| `upNextContainer` | 10 | 4 | 4217–4236, 4262–4288, 5586–5596, 5622 |
| `emby-tab-button` | 9 | 4 | 529, 585, 3394, 5349–5385 |
| `sectionTabs` | 9 | 4 | 1595, 3394, 5219–5224, 5364–5390 |
| `button-link` | 7 | 4 | 529, 556, 2746–2755, 2816–2826 |
| `detailRibbon` | 7 | 4 | 1436–1464, 1631, 1716–1721, 6202 |
| `listItemBodyText` | 7 | 4 | 3646–3665, 3705, 3764, 6104 |
| `visualCardBox` | 7 | 4 | 383, 679–692, 718–723, 847 |
| `detailPagePrimaryContent` | 6 | 4 | 1451–1469, 2171, 4070, 5828 |
| `skip-button` | 6 | 4 | 529, 3399, 4311–4328, 4355–4361 |
| `squareCard` | 6 | 4 | 702, 2219, 2255–2273, 4916–4920 |
| `button-submit` | 5 | 4 | 3415, 3502, 4940–4948, 6177 |
| `mainDrawer` | 5 | 4 | 2760, 5586–5596, 5870, 5909 |
| `sectionTitle` | 5 | 4 | 1571, 1605–1612, 4135, 4907 |
| `skinHeader-blurred` | 5 | 4 | 4854, 5207–5214, 5812, 6069 |
| `appfooter` | 4 | 4 | 2495, 5323, 5673, 6069 |
| `page` | 4 | 4 | 843, 2429, 2474, 5642 |
| `raised` | 4 | 4 | 529, 595, 3282, 3317 |
| `skinHeader-withBackground` | 4 | 4 | 1479, 4854, 5178, 5228 |
| `detailButton` | 12 | 3 | 488–529, 3327–3388, 3444–3448 |
| `emby-scroller` | 9 | 3 | 1576–1590, 5915–5962, 6055–6064 |
| `itemBackdrop` | 9 | 3 | 1763–1807, 1940, 2282 |
| `check` | 8 | 3 | 3109, 3336, 3756–3776 |
| `itemSelectionPanel` | 8 | 3 | 731–735, 3081, 3109–3146 |
| `pageTitle` | 8 | 3 | 1515–1558, 5239, 5298 |
| `detailSectionContent` | 6 | 3 | 2943, 3881–3891, 3972–3982 |
| `emby-checkbox` | 6 | 3 | 3086, 3123–3127, 3170–3182 |
| `headerTop` | 6 | 3 | 5189–5214, 5265–5282, 5309–5313 |
| `actionSheetContent` | 5 | 3 | 3748–3752, 5586–5596, 5622 |
| `cardText-first` | 5 | 3 | 761, 3115–3141, 5021 |
| `dialog` | 5 | 3 | 2993–3003, 5586–5596, 5622 |
| `guideProgramName` | 5 | 3 | 529, 4706–4717, 4760–4765 |
| `musicParentName` | 5 | 3 | 1797, 2277–2282, 4647–4656 |
| `noHomeButtonHeader` | 5 | 3 | 1497, 5239, 5349–5357 |
| `overflowBackdropCard` | 5 | 3 | 800–806, 3119, 5016–5021 |
| `album` | 4 | 3 | 1966, 2224–2228, 2264 |
| `cardPadder` | 4 | 3 | 379, 847, 3132–3136 |
| `cardText` | 4 | 3 | 761–771, 3141, 5988 |
| `cardText-secondary` | 4 | 3 | 761, 3141, 5737–5745 |
| `countIndicator` | 4 | 3 | 639, 5684, 6126–6150 |
| `dialog-fullscreen` | 4 | 3 | 3003, 5586–5596, 5622 |
| `emby-scrollbuttons` | 4 | 3 | 1617–1622, 6000, 6354 |
| `formDialogFooter` | 4 | 3 | 3061, 3509, 6126–6150 |
| `infoWrapper` | 4 | 3 | 1910–1915, 2171, 2199 |
| `listItemImage` | 4 | 3 | 2529–2534, 3619, 6104 |
| `semiTransparent` | 4 | 3 | 1479, 4854, 5207–5228 |
| `toast` | 4 | 3 | 4209, 5586–5596, 5622 |
| `defaultCardBackground` | 3 | 3 | 3257, 5036, 5135 |
| `folder` | 3 | 3 | 1716, 3236, 3300 |
| `formDialogFooterItem` | 3 | 3 | 3061, 3295, 3421 |
| `formDialogHeader` | 3 | 3 | 3509, 6069, 6126 |
| `iconOsd` | 3 | 3 | 4832, 6069, 6126 |
| `itemsContainer` | 3 | 3 | 620, 1599, 4076 |
| `live_tv` | 3 | 3 | 1797, 2264, 3543 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3790, 4084 |
| `playerStats` | 3 | 3 | 4832, 6126, 6162 |
| `scss` | 3 | 3 | 873, 3152, 5759 |
| `sectionTitle-cards` | 3 | 3 | 1571, 4135, 4185 |
| `x` | 3 | 3 | 2037, 4630, 5759 |
| `itemExternalLinks` | 11 | 2 | 2809–2866, 2943 |
| `mdl-slider` | 9 | 2 | 2606, 2661–2719 |
| `listItemIcon` | 8 | 2 | 3539–3543, 3760–3790 |
| `sectionTitleTextButton` | 8 | 2 | 4118–4155, 4189–4199 |
| `sliderContainer` | 8 | 2 | 2610, 2638–2703 |
| `cardOverlayButton-br` | 7 | 2 | 859, 888–926 |
| `detail-clamp-text` | 7 | 2 | 2879–2905, 2931–2935 |
| `backgroundContainer` | 6 | 2 | 2344, 2386–2404 |
| `detailPagePrimaryContainer` | 6 | 2 | 1423–1469, 2171 |
| `detailsGroupItem` | 6 | 2 | 3843, 3911–3949 |
| `divUsers` | 6 | 2 | 4916–4920, 5972–5992 |
| `headerLeft` | 6 | 2 | 1521–1558, 5478 |
| `trackSelections` | 6 | 2 | 3816–3843, 3977–3982 |
| `withBackdrop` | 6 | 2 | 2344, 2386–2404 |
| `detailSection` | 5 | 2 | 3799–3808, 3962–3982 |
| `headerButton` | 5 | 2 | 474–529, 5291 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2769, 5883–5900 |
| `mediaInfoItem` | 5 | 2 | 1635–1678, 5759 |
| `overview-expand` | 5 | 2 | 2911–2935, 3881 |
| `playedIndicator` | 5 | 2 | 3219, 5844–5865 |
| `videoIndicator` | 5 | 2 | 3225–3253, 6126 |
| `withSectionTabs` | 5 | 2 | 2395–2412, 5214 |
| `emby-tab-button-active` | 4 | 2 | 3481, 5376–5390 |
| `play_arrow` | 4 | 2 | 3262–3278, 3448 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3646–3651, 5129–5135 |
| `programCell` | 4 | 2 | 4697, 4756–4765 |
| `programGuideSection` | 4 | 2 | 2232–2247, 3982–3997 |
| `secondary` | 4 | 2 | 3655–3665, 3705 |
| `section0` | 4 | 2 | 813–843, 5642 |
| `visualLoginForm` | 4 | 2 | 4907–4924, 4965 |
| `alphaPickerButton` | 3 | 2 | 529, 4021–4028 |
| `cardFooter` | 3 | 2 | 3146, 5731–5750 |
| `cardOverlayButtonIcon` | 3 | 2 | 859–871, 926 |
| `castCollapsible` | 3 | 2 | 670, 3127–3136 |
| `detailPageContent` | 3 | 2 | 3812, 4063–4070 |
| `emby-scrollbuttons-button` | 3 | 2 | 1626, 6361–6368 |
| `fullSyncIndicator` | 3 | 2 | 639, 6126–6150 |
| `guestCastContent` | 3 | 2 | 670, 3127–3136 |
| `guide-channelHeaderCell` | 3 | 2 | 529, 4731–4747 |
| `guide-date-tab-button` | 3 | 2 | 529, 3481–3489 |
| `manualLoginForm` | 3 | 2 | 4907–4924, 4965 |
| `overview` | 3 | 2 | 2931–2935, 3891 |
| `selectionCommandsPanel` | 3 | 2 | 3071–3077, 6069 |
| `backdropImageFadeIn` | 2 | 2 | 2479, 6166 |
| `blurhash-canvas` | 2 | 2 | 5703, 6112 |
| `book` | 2 | 2 | 1797, 2264 |
| `btnDeleteImage` | 2 | 2 | 3282, 3495 |
| `cardContent` | 2 | 2 | 670, 702 |
| `cardImage` | 2 | 2 | 5703, 6112 |
| `cardOverlayButton` | 2 | 2 | 873, 909 |
| `cardOverlayButton-hover` | 2 | 2 | 756, 888 |
| `chevron_right` | 2 | 2 | 4155, 4199 |
| `collapseContent` | 2 | 2 | 3066, 3507 |
| `content-primary` | 2 | 2 | 4063, 4101 |
| `detailPageSecondaryContainer` | 2 | 2 | 1446, 1473 |
| `editorsChoiceItemOverview` | 2 | 2 | 6291, 6372 |
| `endsAt` | 2 | 2 | 1656, 5759 |
| `formDialogFooter-clear` | 2 | 2 | 3061, 3509 |
| `headerUserButton` | 2 | 2 | 474, 4088 |
| `headroom` | 2 | 2 | 5202, 5239 |
| `mediaInfoOfficialRating` | 2 | 2 | 1656, 5759 |
| `mediaSourceIndicator` | 2 | 2 | 639, 6126 |
| `navMenuOption-selected` | 2 | 2 | 3795, 5894 |
| `nowPlayingInfoContainer` | 2 | 2 | 2800, 5066 |
| `org` | 2 | 2 | 2836, 2866 |
| `paperList` | 2 | 2 | 679, 3520 |
| `playlist` | 2 | 2 | 3641, 5044 |
| `queue` | 2 | 2 | 1797, 2264 |
| `readOnlyContent` | 2 | 2 | 3551, 5407 |
| `recordingFields` | 2 | 2 | 3835, 3977 |
| `runtime` | 2 | 2 | 4977, 5006 |
| `sectionTitleContainer` | 2 | 2 | 1622, 4006 |
| `sectionTitleContainer-cards` | 2 | 2 | 4130, 4185 |
| `tagline` | 2 | 2 | 2335, 3891 |
| `upNextDialog-title` | 2 | 2 | 4241, 4275 |
| `vertical-list` | 2 | 2 | 1599, 6197 |
| `videoOsdBottom` | 2 | 2 | 2792, 5169 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2792, 5169 |
| `checkboxOutline` | 10 | 1 | 3086–3182 |
| `itemDetailsGroup` | 7 | 1 | 3895–3982 |
| `multiSelectCheckboxOutline` | 7 | 1 | 3123–3170 |
| `checkboxContainer` | 6 | 1 | 3115–3146 |
| `trackSelectionFieldContainer` | 6 | 1 | 3854–3877 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6328–6368 |
| `innerCardFooter` | 5 | 1 | 2956–2985 |
| `itemProgressBar` | 5 | 1 | 2529–2552 |
| `backgroundProgress` | 4 | 1 | 2540–2563 |
| `chapterCardImageContainer` | 4 | 1 | 2956–2985 |
| `endTimeText` | 4 | 1 | 4977–5006 |
| `mainDetailButtons` | 4 | 1 | 3444–3458 |
| `overview-controls` | 4 | 1 | 2931–2943 |
| `playbackProgress` | 4 | 1 | 2540–2568 |
| `scrollX` | 4 | 1 | 1576–1595 |
| `startTimeText` | 4 | 1 | 4977–5000 |
| `button-flat` | 3 | 1 | 2773–2783 |
| `cardIndicators` | 3 | 1 | 3199–3209 |
| `cardOverlayFab-primary` | 3 | 1 | 851–873 |
| `com` | 3 | 1 | 2842–2860 |
| `content` | 3 | 1 | 3918–3949 |
| `discover-card` | 3 | 1 | 6379–6402 |
| `emby-select-withcolor` | 3 | 1 | 4455–4489 |
| `emby-textarea` | 3 | 1 | 4446–4471 |
| `fab` | 3 | 1 | 3304–3317 |
| `listChildrenCollapsible` | 3 | 1 | 3967–3982 |
| `mdl-slider-background-flex` | 3 | 1 | 2630–2643 |
| `mediaInfoCriticRating` | 3 | 1 | 1697–1706 |
| `nextUpSection` | 3 | 1 | 3962–3982 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5030–5040 |
| `serverInfo` | 3 | 1 | 3524–3533 |
| `transcodingProgress` | 3 | 1 | 2540–2552 |
