# Index des composants — ElegantFin Cinema Edition v1.3.4

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.4.css` — 6909 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 411–493, 731, 834, 1480–1500, 2003–2036, 2063–2067, 2342–2360, 2396, 5956, 6243–6259, 6339–6361, 6391–6398, 6472, 6787 |
| `cardScalable` | 28 | 13 | 411–422, 470–493, 780–824, 850–888, 2360, 3303, 3414, 3493, 5208, 5970–5980, 6049, 6243, 6382–6398 |
| `cardImageContainer` | 23 | 13 | 465, 802, 830–859, 888, 945–975, 5317–5321, 5402, 5962, 6041–6049, 6102, 6243–6259, 6382, 6520 |
| `material-icons` | 15 | 11 | 347–366, 1699, 1758, 1810, 3260, 3419, 3493–3499, 3605, 3999, 4474, 4508–4518 |
| `itemDetailPage` | 16 | 10 | 1543, 1629, 1708, 1929–1954, 1998, 2098, 2409–2414, 4093, 4381, 6615–6653 |
| `nameContainer` | 27 | 9 | 677, 2105–2128, 2169, 2198, 2233–2279, 2316, 2347–2351, 4847–4899, 6615–6653 |
| `skinHeader` | 16 | 9 | 275, 3849–3884, 5216, 5566, 5622–5630, 5656–5681, 6032, 6211, 6724 |
| `backdropCard` | 12 | 9 | 932–938, 1053, 1929, 2015, 2098, 2351–2360, 2387, 2414, 2684 |
| `card-hoverable` | 23 | 8 | 493, 790, 850–938, 5321, 5980, 6130–6149, 6243, 6527 |
| `parentName` | 23 | 8 | 677, 2110–2128, 2169, 2198, 2233–2279, 4853–4899, 4972, 6615–6653 |
| `detailPageWrapperContainer` | 17 | 8 | 677, 1511–1521, 1954, 2072, 2105–2128, 2198, 2233–2279, 2347 |
| `subtitle` | 16 | 8 | 1929, 1998, 2110, 2169, 2288–2298, 2409–2414, 4907–4940, 6615–6653 |
| `cardBox` | 12 | 8 | 411–459, 485, 731, 872, 979, 5956, 6243, 6527 |
| `detailLogo` | 17 | 7 | 677, 1943–1954, 1989–1998, 2098–2128, 2198, 2233–2279, 2347 |
| `loginPage` | 15 | 7 | 3572, 5220–5235, 5274, 5302–5321, 5985, 6028, 6371–6398 |
| `emby-button` | 10 | 7 | 603–620, 647–665, 3062–3069, 3439, 3474, 3627, 4017 |
| `js` | 7 | 7 | 314, 1615, 2169, 2761, 3393, 6158, 6408 |
| `listItem` | 17 | 6 | 293, 620, 2364, 3919–3945, 3976–4008, 6495–6512 |
| `navMenuOption` | 12 | 6 | 620, 716–726, 3759, 3986–4008, 4074–4079, 6282–6293 |
| `verticalSection` | 11 | 6 | 1703, 2580–2585, 4381, 6041, 6158, 6408 |
| `nowPlayingBar` | 8 | 6 | 2947, 5454, 5995, 6089, 6192–6223, 6477 |
| `person` | 8 | 6 | 1929–1939, 2098, 2351, 2396–2405, 3700, 6610 |
| `mainDrawer` | 7 | 6 | 2911, 3723, 3874, 5985–5995, 6269, 6308 |
| `detailImageContainer` | 20 | 5 | 1929–1939, 2003–2067, 2098, 2338–2360, 2387–2414 |
| `osdHeader` | 15 | 5 | 1672–1690, 5561–5630, 5656–5681, 6032, 6477 |
| `actionSheetMenuItem` | 11 | 5 | 620, 3919–3930, 3976, 4054–4070, 6013 |
| `sectionTabs` | 10 | 5 | 1727, 3551, 3884, 5602–5607, 5747–5773 |
| `cardImageIcon` | 8 | 5 | 403–407, 2351–2360, 2420, 3287, 5402 |
| `paper-icon-button-light` | 8 | 5 | 565–620, 1629, 1699, 1758, 4766 |
| `emby-scroller-container` | 7 | 5 | 1703–1716, 2570, 2606, 6041, 6158 |
| `sectionTitle` | 6 | 5 | 1703, 1737–1744, 3796, 4454, 5269 |
| `portraitCard` | 5 | 5 | 1053, 1131, 1848, 2063, 2684 |
| `scss` | 5 | 5 | 275, 759, 1005, 3309, 6158 |
| `btnPlay` | 16 | 4 | 502–526, 565–620, 3503–3545, 3578–3605 |
| `cardOverlayContainer` | 12 | 4 | 906–938, 983–1005, 1065, 6477–6495 |
| `itemName` | 11 | 4 | 677, 2169, 4853–4899, 4990–5007 |
| `backdropImage` | 10 | 4 | 2486–2513, 2540–2544, 5949, 6049–6057 |
| `emby-tab-button` | 10 | 4 | 620, 687–696, 3551, 5732–5768 |
| `upNextContainer` | 10 | 4 | 4536–4555, 4581–4607, 5985–5995, 6021 |
| `button-link` | 8 | 4 | 620, 647–665, 2897–2906, 2967–2977 |
| `headerTop` | 8 | 4 | 3849–3874, 5572–5597, 5648–5665, 5692–5696 |
| `detailRibbon` | 7 | 4 | 1568–1596, 1763, 1848–1853, 6610 |
| `listItemBodyText` | 7 | 4 | 3940–3959, 3999, 4058, 6512 |
| `visualCardBox` | 7 | 4 | 411, 811–824, 850–855, 979 |
| `cardText-secondary` | 6 | 4 | 293, 893, 3292–3296, 6136–6144 |
| `detailPagePrimaryContent` | 6 | 4 | 1583–1601, 2303, 4375, 6227 |
| `skip-button` | 6 | 4 | 620, 3556, 4630–4647, 4674–4680 |
| `squareCard` | 6 | 4 | 834, 2351, 2387–2405, 5278–5282 |
| `button-submit` | 5 | 4 | 3572, 3659, 5302–5310, 6585 |
| `skinHeader-blurred` | 5 | 4 | 5216, 5590–5597, 6211, 6477 |
| `appfooter` | 4 | 4 | 2627, 5706, 6072, 6477 |
| `page` | 4 | 4 | 975, 2561, 2606, 6041 |
| `raised` | 4 | 4 | 620, 706, 3439, 3474 |
| `skinHeader-withBackground` | 4 | 4 | 1611, 5216, 5561, 5611 |
| `detailButton` | 13 | 3 | 565–620, 3484–3545, 3601–3605 |
| `emby-scroller` | 9 | 3 | 1708–1722, 6314–6361, 6463–6472 |
| `itemBackdrop` | 9 | 3 | 1895–1939, 2072, 2414 |
| `itemSelectionPanel` | 9 | 3 | 863–867, 3232, 3260–3303 |
| `check` | 8 | 3 | 3260, 3493, 4050–4070 |
| `pageTitle` | 8 | 3 | 1647–1690, 5622, 5681 |
| `playedIndicator` | 7 | 3 | 759–773, 3376, 6243–6264 |
| `countIndicator` | 6 | 3 | 750–773, 6083, 6534–6558 |
| `detailSectionContent` | 6 | 3 | 3094, 4175–4185, 4266–4276 |
| `emby-checkbox` | 6 | 3 | 3237, 3274–3278, 3327–3339 |
| `actionSheetContent` | 5 | 3 | 4042–4046, 5985–5995, 6021 |
| `cardText-first` | 5 | 3 | 893, 3266–3292, 5383 |
| `dialog` | 5 | 3 | 3144–3154, 5985–5995, 6021 |
| `guideProgramName` | 5 | 3 | 620, 5031–5042, 5085–5090 |
| `musicParentName` | 5 | 3 | 1929, 2409–2414, 4972–4981 |
| `noHomeButtonHeader` | 5 | 3 | 1629, 5622, 5732–5740 |
| `overflowBackdropCard` | 5 | 3 | 932–938, 3270, 5378–5383 |
| `secondary` | 5 | 3 | 293, 3949–3959, 3999 |
| `album` | 4 | 3 | 2098, 2356–2360, 2396 |
| `cardPadder` | 4 | 3 | 407, 979, 3283–3287 |
| `cardText` | 4 | 3 | 893–903, 3292, 6387 |
| `dialog-fullscreen` | 4 | 3 | 3154, 5985–5995, 6021 |
| `emby-scrollbuttons` | 4 | 3 | 1749–1754, 6408, 6762 |
| `formDialogFooter` | 4 | 3 | 3212, 3666, 6534–6558 |
| `infoWrapper` | 4 | 3 | 2042–2047, 2303, 2331 |
| `listItemImage` | 4 | 3 | 2661–2666, 3913, 6512 |
| `semiTransparent` | 4 | 3 | 1611, 5216, 5590–5611 |
| `toast` | 4 | 3 | 4528, 5985–5995, 6021 |
| `defaultCardBackground` | 3 | 3 | 3414, 5398, 5497 |
| `folder` | 3 | 3 | 1848, 3393, 3457 |
| `formDialogFooterItem` | 3 | 3 | 3212, 3452, 3578 |
| `formDialogHeader` | 3 | 3 | 3666, 6477, 6534 |
| `iconOsd` | 3 | 3 | 5194, 6477, 6534 |
| `itemsContainer` | 3 | 3 | 731, 1731, 4381 |
| `live_tv` | 3 | 3 | 1929, 2396, 3700 |
| `myPreferencesMenuPage` | 3 | 3 | 380, 4084, 4389 |
| `playerStats` | 3 | 3 | 5194, 6534, 6570 |
| `sectionTitle-cards` | 3 | 3 | 1703, 4454, 4504 |
| `x` | 3 | 3 | 2169, 4955, 6158 |
| `itemExternalLinks` | 11 | 2 | 2960–3017, 3094 |
| `checkboxOutline` | 10 | 2 | 3237–3278, 3309–3339 |
| `mdl-slider` | 9 | 2 | 2757, 2812–2870 |
| `listItemIcon` | 8 | 2 | 3696–3700, 4054–4084 |
| `sectionTitleTextButton` | 8 | 2 | 4437–4474, 4508–4518 |
| `sliderContainer` | 8 | 2 | 2761, 2789–2854 |
| `cardOverlayButton-br` | 7 | 2 | 991, 1020–1058 |
| `detail-clamp-text` | 7 | 2 | 3030–3056, 3082–3086 |
| `divUsers` | 7 | 2 | 5278–5282, 6371–6398 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3274–3278, 3308–3327 |
| `backgroundContainer` | 6 | 2 | 2476, 2518–2536 |
| `detailPagePrimaryContainer` | 6 | 2 | 1555–1601, 2303 |
| `detailsGroupItem` | 6 | 2 | 4137, 4205–4243 |
| `headerButton` | 6 | 2 | 540–620, 5674 |
| `headerLeft` | 6 | 2 | 1653–1690, 5877 |
| `trackSelections` | 6 | 2 | 4110–4137, 4271–4276 |
| `withBackdrop` | 6 | 2 | 2476, 2518–2536 |
| `detailSection` | 5 | 2 | 4093–4102, 4256–4276 |
| `fullSyncIndicator` | 5 | 2 | 750–773, 6534–6558 |
| `homePage` | 5 | 2 | 3849–3884, 5790 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2920, 6282–6299 |
| `mediaInfoItem` | 5 | 2 | 1767–1810, 6158 |
| `overview-expand` | 5 | 2 | 3062–3086, 4175 |
| `videoIndicator` | 5 | 2 | 3382–3410, 6534 |
| `withSectionTabs` | 5 | 2 | 2527–2544, 5597 |
| `alphaPickerButton` | 4 | 2 | 620, 4315–4327 |
| `backgroundProgress` | 4 | 2 | 2672–2684, 2714 |
| `emby-tab-button-active` | 4 | 2 | 3638, 5759–5773 |
| `mediaSourceIndicator` | 4 | 2 | 750–773, 6534 |
| `play_arrow` | 4 | 2 | 3419–3435, 3605 |
| `playbackProgress` | 4 | 2 | 2672–2684, 2719 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3940–3945, 5491–5497 |
| `programCell` | 4 | 2 | 5022, 5081–5090 |
| `programGuideSection` | 4 | 2 | 2364–2379, 4276–4291 |
| `section0` | 4 | 2 | 945–975, 6041 |
| `visualLoginForm` | 4 | 2 | 5269–5286, 5327 |
| `cardFooter` | 3 | 2 | 3303, 6130–6149 |
| `cardOverlayButtonIcon` | 3 | 2 | 991–1003, 1058 |
| `castCollapsible` | 3 | 2 | 802, 3278–3287 |
| `detailPageContent` | 3 | 2 | 4106, 4368–4375 |
| `emby-scrollbuttons-button` | 3 | 2 | 1758, 6769–6776 |
| `guestCastContent` | 3 | 2 | 802, 3278–3287 |
| `guide-channelHeaderCell` | 3 | 2 | 620, 5056–5072 |
| `guide-date-tab-button` | 3 | 2 | 620, 3638–3646 |
| `headerUserButton` | 3 | 2 | 540–553, 4393 |
| `manualLoginForm` | 3 | 2 | 5269–5286, 5327 |
| `overview` | 3 | 2 | 3082–3086, 4185 |
| `selectionCommandsPanel` | 3 | 2 | 3222–3228, 6477 |
| `backdropImageFadeIn` | 2 | 2 | 2611, 6574 |
| `blurhash-canvas` | 2 | 2 | 6102, 6520 |
| `book` | 2 | 2 | 1929, 2396 |
| `btnDeleteImage` | 2 | 2 | 3439, 3652 |
| `cardContent` | 2 | 2 | 802, 834 |
| `cardImage` | 2 | 2 | 6102, 6520 |
| `cardOverlayButton` | 2 | 2 | 1005, 1041 |
| `cardOverlayButton-hover` | 2 | 2 | 888, 1020 |
| `chevron_right` | 2 | 2 | 4474, 4518 |
| `collapseContent` | 2 | 2 | 3217, 3664 |
| `content-primary` | 2 | 2 | 4368, 4420 |
| `detailPageSecondaryContainer` | 2 | 2 | 1578, 1605 |
| `editorsChoiceItemOverview` | 2 | 2 | 6699, 6780 |
| `endsAt` | 2 | 2 | 1788, 6158 |
| `formDialogFooter-clear` | 2 | 2 | 3212, 3666 |
| `guide-programNameCaret` | 2 | 2 | 293, 5038 |
| `headroom` | 2 | 2 | 5585, 5622 |
| `mediaInfoOfficialRating` | 2 | 2 | 1788, 6158 |
| `navMenuOption-selected` | 2 | 2 | 4089, 6293 |
| `nowPlayingInfoContainer` | 2 | 2 | 2951, 5428 |
| `org` | 2 | 2 | 2987, 3017 |
| `paperList` | 2 | 2 | 811, 3677 |
| `playlist` | 2 | 2 | 3935, 5406 |
| `queue` | 2 | 2 | 1929, 2396 |
| `readOnlyContent` | 2 | 2 | 3708, 5806 |
| `recordingFields` | 2 | 2 | 4129, 4271 |
| `runtime` | 2 | 2 | 5339, 5368 |
| `sectionTitleContainer` | 2 | 2 | 1754, 4300 |
| `sectionTitleContainer-cards` | 2 | 2 | 4449, 4504 |
| `sidebarHeader` | 2 | 2 | 3746, 6299 |
| `tagline` | 2 | 2 | 2467, 4185 |
| `tsx` | 2 | 2 | 3849, 3888 |
| `upNextDialog-title` | 2 | 2 | 4560, 4594 |
| `vertical-list` | 2 | 2 | 1731, 6605 |
| `videoOsdBottom` | 2 | 2 | 2943, 5552 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2943, 5552 |
| `checkboxContainer` | 7 | 1 | 3266–3303 |
| `itemDetailsGroup` | 7 | 1 | 4189–4276 |
| `itemProgressBar` | 6 | 1 | 2661–2695 |
| `trackSelectionFieldContainer` | 6 | 1 | 4148–4171 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6736–6776 |
| `innerCardFooter` | 5 | 1 | 3107–3136 |
| `chapterCardImageContainer` | 4 | 1 | 3107–3136 |
| `endTimeText` | 4 | 1 | 5339–5368 |
| `mainDetailButtons` | 4 | 1 | 3601–3615 |
| `overview-controls` | 4 | 1 | 3082–3094 |
| `scrollX` | 4 | 1 | 1708–1727 |
| `startTimeText` | 4 | 1 | 5339–5362 |
| `button-flat` | 3 | 1 | 2924–2934 |
| `cardIndicators` | 3 | 1 | 3356–3366 |
| `cardOverlayFab-primary` | 3 | 1 | 983–1005 |
| `com` | 3 | 1 | 2993–3011 |
| `content` | 3 | 1 | 4212–4243 |
| `discover-card` | 3 | 1 | 6787–6810 |
| `emby-select-withcolor` | 3 | 1 | 4780–4814 |
| `emby-textarea` | 3 | 1 | 4771–4796 |
| `fab` | 3 | 1 | 3461–3474 |
| `listChildrenCollapsible` | 3 | 1 | 4261–4276 |
| `mdl-slider-background-flex` | 3 | 1 | 2781–2794 |
| `mediaInfoCriticRating` | 3 | 1 | 1829–1838 |
| `nextUpSection` | 3 | 1 | 4256–4276 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5392–5402 |
| `serverInfo` | 3 | 1 | 3681–3690 |
| `transcodingProgress` | 3 | 1 | 2672–2684 |
