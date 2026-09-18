# Index des composants — ElegantFin Cinema Edition v1.3.4

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.4.css` — 7131 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 411–493, 731, 834, 1480–1500, 2003–2036, 2063–2067, 2342–2360, 2396, 6083, 6370–6386, 6466–6488, 6518–6525, 6599, 7009 |
| `cardScalable` | 28 | 13 | 411–422, 470–493, 780–824, 850–888, 2360, 3303, 3414, 3493, 5308, 6097–6107, 6176, 6370, 6509–6525 |
| `cardImageContainer` | 23 | 13 | 465, 802, 830–859, 888, 945–975, 5417–5421, 5502, 6089, 6168–6176, 6229, 6370–6386, 6509, 6647 |
| `material-icons` | 16 | 12 | 347–366, 1699, 1758, 1810, 3260, 3419, 3493–3499, 3605, 3763, 4099, 4574, 4608–4618 |
| `itemDetailPage` | 18 | 11 | 1543, 1629, 1708, 1929–1954, 1998, 2098, 2409–2414, 3748–3759, 4193, 4481, 6837–6875 |
| `nameContainer` | 27 | 9 | 677, 2105–2128, 2169, 2198, 2233–2279, 2316, 2347–2351, 4947–4999, 6837–6875 |
| `skinHeader` | 16 | 9 | 275, 3932–3984, 5316, 5693, 5749–5757, 5783–5808, 6159, 6338, 6946 |
| `backdropCard` | 12 | 9 | 932–938, 1053, 1929, 2015, 2098, 2351–2360, 2387, 2414, 2684 |
| `card-hoverable` | 23 | 8 | 493, 790, 850–938, 5421, 6107, 6257–6276, 6370, 6654 |
| `parentName` | 23 | 8 | 677, 2110–2128, 2169, 2198, 2233–2279, 4953–4999, 5072, 6837–6875 |
| `detailPageWrapperContainer` | 17 | 8 | 677, 1511–1521, 1954, 2072, 2105–2128, 2198, 2233–2279, 2347 |
| `subtitle` | 16 | 8 | 1929, 1998, 2110, 2169, 2288–2298, 2409–2414, 5007–5040, 6837–6875 |
| `cardBox` | 12 | 8 | 411–459, 485, 731, 872, 979, 6083, 6370, 6654 |
| `detailLogo` | 17 | 7 | 677, 1943–1954, 1989–1998, 2098–2128, 2198, 2233–2279, 2347 |
| `loginPage` | 15 | 7 | 3572, 5320–5335, 5374, 5402–5421, 6112, 6155, 6498–6525 |
| `emby-button` | 10 | 7 | 603–620, 647–665, 3062–3069, 3439, 3474, 3627, 4117 |
| `js` | 7 | 7 | 314, 1615, 2169, 2761, 3393, 6285, 6535 |
| `listItem` | 17 | 6 | 293, 620, 2364, 4019–4045, 4076–4108, 6622–6639 |
| `navMenuOption` | 12 | 6 | 620, 716–726, 3813, 4086–4108, 4174–4179, 6409–6420 |
| `verticalSection` | 11 | 6 | 1703, 2580–2585, 4481, 6168, 6285, 6535 |
| `nowPlayingBar` | 8 | 6 | 2947, 5554, 6122, 6216, 6319–6350, 6604 |
| `person` | 8 | 6 | 1929–1939, 2098, 2351, 2396–2405, 3700, 6832 |
| `mainDrawer` | 7 | 6 | 2911, 3777, 3957, 6112–6122, 6396, 6435 |
| `detailImageContainer` | 20 | 5 | 1929–1939, 2003–2067, 2098, 2338–2360, 2387–2414 |
| `osdHeader` | 15 | 5 | 1672–1690, 5688–5757, 5783–5808, 6159, 6604 |
| `actionSheetMenuItem` | 11 | 5 | 620, 4019–4030, 4076, 4154–4170, 6140 |
| `sectionTabs` | 10 | 5 | 1727, 3551, 3984, 5729–5734, 5874–5900 |
| `button-link` | 9 | 5 | 620, 647–665, 2897–2906, 2967–2977, 6800 |
| `cardImageIcon` | 8 | 5 | 403–407, 2351–2360, 2420, 3287, 5502 |
| `paper-icon-button-light` | 8 | 5 | 565–620, 1629, 1699, 1758, 4866 |
| `emby-scroller-container` | 7 | 5 | 1703–1716, 2570, 2606, 6168, 6285 |
| `sectionTitle` | 6 | 5 | 1703, 1737–1744, 3879, 4554, 5369 |
| `portraitCard` | 5 | 5 | 1053, 1131, 1848, 2063, 2684 |
| `scss` | 5 | 5 | 275, 759, 1005, 3309, 6285 |
| `skinHeader-withBackground` | 5 | 5 | 1611, 3748, 5316, 5688, 5738 |
| `btnPlay` | 16 | 4 | 502–526, 565–620, 3503–3545, 3578–3605 |
| `cardOverlayContainer` | 12 | 4 | 906–938, 983–1005, 1065, 6604–6622 |
| `itemName` | 11 | 4 | 677, 2169, 4953–4999, 5090–5107 |
| `backdropImage` | 10 | 4 | 2486–2513, 2540–2544, 6076, 6176–6184 |
| `emby-tab-button` | 10 | 4 | 620, 687–696, 3551, 5859–5895 |
| `upNextContainer` | 10 | 4 | 4636–4655, 4681–4707, 6112–6122, 6148 |
| `headerTop` | 8 | 4 | 3932–3957, 5699–5724, 5775–5792, 5819–5823 |
| `detailRibbon` | 7 | 4 | 1568–1596, 1763, 1848–1853, 6832 |
| `listItemBodyText` | 7 | 4 | 4040–4059, 4099, 4158, 6639 |
| `visualCardBox` | 7 | 4 | 411, 811–824, 850–855, 979 |
| `button-submit` | 6 | 4 | 3572, 3659, 5402–5410, 6712–6726 |
| `cardText-secondary` | 6 | 4 | 293, 893, 3292–3296, 6263–6271 |
| `detailPagePrimaryContent` | 6 | 4 | 1583–1601, 2303, 4475, 6354 |
| `skip-button` | 6 | 4 | 620, 3556, 4730–4747, 4774–4780 |
| `squareCard` | 6 | 4 | 834, 2351, 2387–2405, 5378–5382 |
| `skinHeader-blurred` | 5 | 4 | 5316, 5717–5724, 6338, 6604 |
| `appfooter` | 4 | 4 | 2627, 5833, 6199, 6604 |
| `page` | 4 | 4 | 975, 2561, 2606, 6168 |
| `raised` | 4 | 4 | 620, 706, 3439, 3474 |
| `detailButton` | 13 | 3 | 565–620, 3484–3545, 3601–3605 |
| `emby-scroller` | 9 | 3 | 1708–1722, 6441–6488, 6590–6599 |
| `itemBackdrop` | 9 | 3 | 1895–1939, 2072, 2414 |
| `itemSelectionPanel` | 9 | 3 | 863–867, 3232, 3260–3303 |
| `check` | 8 | 3 | 3260, 3493, 4150–4170 |
| `pageTitle` | 8 | 3 | 1647–1690, 5749, 5808 |
| `playedIndicator` | 7 | 3 | 759–773, 3376, 6370–6391 |
| `countIndicator` | 6 | 3 | 750–773, 6210, 6661–6685 |
| `detailSectionContent` | 6 | 3 | 3094, 4275–4285, 4366–4376 |
| `emby-checkbox` | 6 | 3 | 3237, 3274–3278, 3327–3339 |
| `actionSheetContent` | 5 | 3 | 4142–4146, 6112–6122, 6148 |
| `cardText-first` | 5 | 3 | 893, 3266–3292, 5483 |
| `dialog` | 5 | 3 | 3144–3154, 6112–6122, 6148 |
| `guideProgramName` | 5 | 3 | 620, 5131–5142, 5185–5190 |
| `musicParentName` | 5 | 3 | 1929, 2409–2414, 5072–5081 |
| `noHomeButtonHeader` | 5 | 3 | 1629, 5749, 5859–5867 |
| `overflowBackdropCard` | 5 | 3 | 932–938, 3270, 5478–5483 |
| `secondary` | 5 | 3 | 293, 4049–4059, 4099 |
| `album` | 4 | 3 | 2098, 2356–2360, 2396 |
| `cardPadder` | 4 | 3 | 407, 979, 3283–3287 |
| `cardText` | 4 | 3 | 893–903, 3292, 6514 |
| `dialog-fullscreen` | 4 | 3 | 3154, 6112–6122, 6148 |
| `emby-scrollbuttons` | 4 | 3 | 1749–1754, 6535, 6984 |
| `formDialogFooter` | 4 | 3 | 3212, 3666, 6661–6685 |
| `infoWrapper` | 4 | 3 | 2042–2047, 2303, 2331 |
| `listItemImage` | 4 | 3 | 2661–2666, 4013, 6639 |
| `semiTransparent` | 4 | 3 | 1611, 5316, 5717–5738 |
| `toast` | 4 | 3 | 4628, 6112–6122, 6148 |
| `defaultCardBackground` | 3 | 3 | 3414, 5498, 5597 |
| `folder` | 3 | 3 | 1848, 3393, 3457 |
| `formDialogFooterItem` | 3 | 3 | 3212, 3452, 3578 |
| `formDialogHeader` | 3 | 3 | 3666, 6604, 6661 |
| `iconOsd` | 3 | 3 | 5294, 6604, 6661 |
| `itemsContainer` | 3 | 3 | 731, 1731, 4481 |
| `live_tv` | 3 | 3 | 1929, 2396, 3700 |
| `myPreferencesMenuPage` | 3 | 3 | 380, 4184, 4489 |
| `playerStats` | 3 | 3 | 5294, 6661, 6697 |
| `sectionTitle-cards` | 3 | 3 | 1703, 4554, 4604 |
| `x` | 3 | 3 | 2169, 5055, 6285 |
| `itemExternalLinks` | 11 | 2 | 2960–3017, 3094 |
| `checkboxOutline` | 10 | 2 | 3237–3278, 3309–3339 |
| `mdl-slider` | 9 | 2 | 2757, 2812–2870 |
| `listItemIcon` | 8 | 2 | 3696–3700, 4154–4184 |
| `sectionTitleTextButton` | 8 | 2 | 4537–4574, 4608–4618 |
| `sliderContainer` | 8 | 2 | 2761, 2789–2854 |
| `cardOverlayButton-br` | 7 | 2 | 991, 1020–1058 |
| `detail-clamp-text` | 7 | 2 | 3030–3056, 3082–3086 |
| `divUsers` | 7 | 2 | 5378–5382, 6498–6525 |
| `homePage` | 7 | 2 | 3932–3984, 5917 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3274–3278, 3308–3327 |
| `backgroundContainer` | 6 | 2 | 2476, 2518–2536 |
| `detailPagePrimaryContainer` | 6 | 2 | 1555–1601, 2303 |
| `detailsGroupItem` | 6 | 2 | 4237, 4305–4343 |
| `headerButton` | 6 | 2 | 540–620, 5801 |
| `headerLeft` | 6 | 2 | 1653–1690, 6004 |
| `trackSelections` | 6 | 2 | 4210–4237, 4371–4376 |
| `withBackdrop` | 6 | 2 | 2476, 2518–2536 |
| `detailSection` | 5 | 2 | 4193–4202, 4356–4376 |
| `fullSyncIndicator` | 5 | 2 | 750–773, 6661–6685 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2920, 6409–6426 |
| `mediaInfoItem` | 5 | 2 | 1767–1810, 6285 |
| `overview-expand` | 5 | 2 | 3062–3086, 4275 |
| `videoIndicator` | 5 | 2 | 3382–3410, 6661 |
| `withSectionTabs` | 5 | 2 | 2527–2544, 5724 |
| `alphaPickerButton` | 4 | 2 | 620, 4415–4427 |
| `backgroundProgress` | 4 | 2 | 2672–2684, 2714 |
| `emby-tab-button-active` | 4 | 2 | 3638, 5886–5900 |
| `mediaSourceIndicator` | 4 | 2 | 750–773, 6661 |
| `play_arrow` | 4 | 2 | 3419–3435, 3605 |
| `playbackProgress` | 4 | 2 | 2672–2684, 2719 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4040–4045, 5591–5597 |
| `programCell` | 4 | 2 | 5122, 5181–5190 |
| `programGuideSection` | 4 | 2 | 2364–2379, 4376–4391 |
| `section0` | 4 | 2 | 945–975, 6168 |
| `visualLoginForm` | 4 | 2 | 5369–5386, 5427 |
| `cardFooter` | 3 | 2 | 3303, 6257–6276 |
| `cardOverlayButtonIcon` | 3 | 2 | 991–1003, 1058 |
| `castCollapsible` | 3 | 2 | 802, 3278–3287 |
| `detailPageContent` | 3 | 2 | 4206, 4468–4475 |
| `emby-input` | 3 | 2 | 4880–4896, 6726 |
| `emby-scrollbuttons-button` | 3 | 2 | 1758, 6991–6998 |
| `guestCastContent` | 3 | 2 | 802, 3278–3287 |
| `guide-channelHeaderCell` | 3 | 2 | 620, 5156–5172 |
| `guide-date-tab-button` | 3 | 2 | 620, 3638–3646 |
| `headerUserButton` | 3 | 2 | 540–553, 4493 |
| `manualLoginForm` | 3 | 2 | 5369–5386, 5427 |
| `overview` | 3 | 2 | 3082–3086, 4285 |
| `selectionCommandsPanel` | 3 | 2 | 3222–3228, 6604 |
| `backdropImageFadeIn` | 2 | 2 | 2611, 6701 |
| `blurhash-canvas` | 2 | 2 | 6229, 6647 |
| `book` | 2 | 2 | 1929, 2396 |
| `btnDeleteImage` | 2 | 2 | 3439, 3652 |
| `cardContent` | 2 | 2 | 802, 834 |
| `cardImage` | 2 | 2 | 6229, 6647 |
| `cardOverlayButton` | 2 | 2 | 1005, 1041 |
| `cardOverlayButton-hover` | 2 | 2 | 888, 1020 |
| `chevron_right` | 2 | 2 | 4574, 4618 |
| `collapseContent` | 2 | 2 | 3217, 3664 |
| `content-primary` | 2 | 2 | 4468, 4520 |
| `detailPageSecondaryContainer` | 2 | 2 | 1578, 1605 |
| `editorsChoiceItemOverview` | 2 | 2 | 6921, 7002 |
| `emby-select` | 2 | 2 | 4880, 6726 |
| `endsAt` | 2 | 2 | 1788, 6285 |
| `fieldDescription` | 2 | 2 | 293, 6726 |
| `formDialogFooter-clear` | 2 | 2 | 3212, 3666 |
| `guide-programNameCaret` | 2 | 2 | 293, 5138 |
| `headroom` | 2 | 2 | 5712, 5749 |
| `mediaInfoOfficialRating` | 2 | 2 | 1788, 6285 |
| `navMenuOption-selected` | 2 | 2 | 4189, 6420 |
| `nowPlayingInfoContainer` | 2 | 2 | 2951, 5528 |
| `org` | 2 | 2 | 2987, 3017 |
| `paperList` | 2 | 2 | 811, 3677 |
| `playlist` | 2 | 2 | 4035, 5506 |
| `queue` | 2 | 2 | 1929, 2396 |
| `readOnlyContent` | 2 | 2 | 3708, 5933 |
| `recordingFields` | 2 | 2 | 4229, 4371 |
| `runtime` | 2 | 2 | 5439, 5468 |
| `sectionTitleContainer` | 2 | 2 | 1754, 4400 |
| `sectionTitleContainer-cards` | 2 | 2 | 4549, 4604 |
| `sidebarHeader` | 2 | 2 | 3800, 6426 |
| `tagline` | 2 | 2 | 2467, 4285 |
| `tsx` | 2 | 2 | 3932, 3988 |
| `upNextDialog-title` | 2 | 2 | 4660, 4694 |
| `vertical-list` | 2 | 2 | 1731, 6827 |
| `videoOsdBottom` | 2 | 2 | 2943, 5679 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2943, 5679 |
| `userPreferencesPage` | 12 | 1 | 6712–6807 |
| `checkboxContainer` | 7 | 1 | 3266–3303 |
| `itemDetailsGroup` | 7 | 1 | 4289–4376 |
| `itemProgressBar` | 6 | 1 | 2661–2695 |
| `trackSelectionFieldContainer` | 6 | 1 | 4248–4271 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6958–6998 |
| `innerCardFooter` | 5 | 1 | 3107–3136 |
| `chapterCardImageContainer` | 4 | 1 | 3107–3136 |
| `endTimeText` | 4 | 1 | 5439–5468 |
| `mainDetailButtons` | 4 | 1 | 3601–3615 |
| `overview-controls` | 4 | 1 | 3082–3094 |
| `scrollX` | 4 | 1 | 1708–1727 |
| `startTimeText` | 4 | 1 | 5439–5462 |
| `button-flat` | 3 | 1 | 2924–2934 |
| `cardIndicators` | 3 | 1 | 3356–3366 |
| `cardOverlayFab-primary` | 3 | 1 | 983–1005 |
| `com` | 3 | 1 | 2993–3011 |
| `content` | 3 | 1 | 4312–4343 |
| `discover-card` | 3 | 1 | 7009–7032 |
| `emby-select-withcolor` | 3 | 1 | 4880–4914 |
| `emby-textarea` | 3 | 1 | 4871–4896 |
| `fab` | 3 | 1 | 3461–3474 |
| `listChildrenCollapsible` | 3 | 1 | 4361–4376 |
| `mdl-slider-background-flex` | 3 | 1 | 2781–2794 |
| `mediaInfoCriticRating` | 3 | 1 | 1829–1838 |
| `nextUpSection` | 3 | 1 | 4356–4376 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5492–5502 |
| `serverInfo` | 3 | 1 | 3681–3690 |
| `transcodingProgress` | 3 | 1 | 2672–2684 |
