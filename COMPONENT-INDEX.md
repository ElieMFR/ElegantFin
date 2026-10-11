# Index des composants — ElegantFin Cinema Edition v1.3.25

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.25.css` — 7871 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2128–2161, 2188–2192, 2469–2487, 2523, 6764, 7022–7041, 7119–7141, 7171–7178, 7342, 7749 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2487, 3567, 3678, 3757, 5911, 6778–6788, 6857, 7022, 7162–7178 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2001–2037, 2072–2087, 2123, 2224, 2536, 4013–4024, 4684, 4983, 7577–7615 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1887, 3524, 3683, 3757–3763, 3870, 4028, 4561, 5090, 5124–5134, 5728 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 6037–6041, 6121, 6770, 6849–6857, 6897, 7022–7041, 7162 |
| `skinHeader` | 16 | 10 | 284, 4373, 4419–4446, 5919, 6330, 6386–6394, 6460–6485, 6840, 6989, 7686 |
| `nameContainer` | 27 | 9 | 694, 2231–2254, 2295, 2324, 2359–2406, 2443, 2474–2478, 5484–5537, 7577–7615 |
| `emby-button` | 12 | 9 | 620–637, 664–682, 3163, 3298–3305, 3703, 3738, 3892, 4579, 5306 |
| `js` | 9 | 9 | 331, 1652, 1745, 2295, 2901, 3657, 5728, 6941, 7188 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 6041, 6788, 6897–6932, 7022, 7388 |
| `parentName` | 23 | 8 | 694, 2236–2254, 2295, 2324, 2359–2406, 5490–5537, 5610, 7577–7615 |
| `detailLogo` | 20 | 8 | 694, 2011–2037, 2072–2087, 2114–2123, 2224–2254, 2324, 2359–2406, 2474 |
| `listItem` | 19 | 8 | 302, 637, 2491, 4481–4507, 4538–4570, 4615, 4659, 7365–7382 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2037, 2197, 2231–2254, 2324, 2359–2406, 2474 |
| `subtitle` | 16 | 8 | 2001–2011, 2123, 2236, 2295, 2415–2425, 2536, 5545–5578, 7577–7615 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2001–2011, 2140, 2224, 2478–2487, 2514, 2824 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6764, 7022, 7388 |
| `nowPlayingBar` | 8 | 8 | 318, 3087, 6173, 6803, 6891, 6975, 7001, 7347 |
| `loginPage` | 16 | 7 | 3836, 5923–5954, 5994, 6022–6041, 6793, 6836, 7151–7178 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4078, 4548–4570, 4665–4670, 7064–7075 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3464–3484, 5390 |
| `verticalSection` | 11 | 6 | 1740, 2726–2731, 4983, 6849, 6941, 7188 |
| `button-link` | 10 | 6 | 637, 664–682, 3037–3046, 3107–3117, 3163, 7539 |
| `person` | 8 | 6 | 2001–2022, 2224, 2478, 2523–2532, 3965, 7572 |
| `mainDrawer` | 7 | 6 | 3051, 4042, 4419, 6793–6803, 7051, 7090 |
| `scss` | 6 | 6 | 284, 776, 1036, 3573, 4084, 6941 |
| `detailImageContainer` | 20 | 5 | 2001–2022, 2128–2192, 2224, 2465–2487, 2514–2532 |
| `osdHeader` | 15 | 5 | 1709–1727, 6325–6394, 6460–6485, 6840, 7347 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4481–4492, 4538, 4615–4659, 6821 |
| `sectionTabs` | 10 | 5 | 1803, 3815, 4446, 6366–6371, 6551–6582 |
| `cardImageIcon` | 8 | 5 | 420–424, 2478–2487, 2550, 3551, 6121 |
| `headerTop` | 8 | 5 | 4373, 4419, 6336–6361, 6452–6469, 6496–6500 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4274, 5060–5068, 5989 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2716, 6849, 6941 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1925–1930, 2188, 2824 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 4013, 5919, 6325, 6375 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3767–3809, 3842–3870 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7347–7365 |
| `itemName` | 11 | 4 | 694, 2295, 5490–5537, 5628–5645 |
| `backdropImage` | 10 | 4 | 2615–2643, 2670–2674, 6757, 6857–6865 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3815, 6536–6577 |
| `upNextContainer` | 10 | 4 | 5152–5171, 5197–5223, 6793–6803, 6829 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 7094–7141, 7326–7342 |
| `backgroundContainer` | 8 | 4 | 2091, 2606, 2648–2666, 2698 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1840, 1925–1937, 7572 |
| `listItemBodyText` | 7 | 4 | 4502–4521, 4561, 4636, 7382 |
| `skip-button` | 7 | 4 | 637, 3820, 5246–5263, 5290–5308 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3836, 3924, 6022–6030, 7450–7465 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3556–3560, 6919–6927 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2430, 4977, 7005 |
| `squareCard` | 6 | 4 | 865, 2478, 2514–2532, 5998–6002 |
| `semiTransparent` | 5 | 4 | 1648, 5919, 6354–6375, 6411 |
| `skinHeader-blurred` | 5 | 4 | 5919, 6354–6361, 6989, 7347 |
| `appfooter` | 4 | 4 | 2767, 6510, 6880, 7347 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4983 |
| `raised` | 4 | 4 | 637, 723, 3703, 3738 |
| `x` | 4 | 4 | 2295, 4084, 5593, 6941 |
| `detailButton` | 13 | 3 | 582–637, 3748–3809, 3866–3870 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3496, 3524–3567 |
| `pageTitle` | 8 | 3 | 1684–1727, 6386, 6485 |
| `sectionTitleTextButton` | 8 | 3 | 5043–5051, 5078–5090, 5124–5134 |
| `homePage` | 7 | 3 | 4373, 4419–4446, 6599 |
| `playedIndicator` | 7 | 3 | 776–790, 3640, 7022–7046 |
| `check` | 6 | 3 | 3524, 3757, 4615–4659 |
| `detailSectionContent` | 6 | 3 | 3330, 4766–4776, 4856–4866 |
| `emby-checkbox` | 6 | 3 | 3501, 3538–3542, 3591–3603 |
| `actionSheetContent` | 5 | 3 | 4607–4611, 6793–6803, 6829 |
| `cardText-first` | 5 | 3 | 924, 3530–3556, 6102 |
| `dialog` | 5 | 3 | 3380–3390, 6793–6803, 6829 |
| `guideProgramName` | 5 | 3 | 637, 5669–5680, 5723–5728 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6386, 6536–6544 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3534, 6097–6102 |
| `secondary` | 5 | 3 | 302, 4511–4521, 4561 |
| `album` | 4 | 3 | 2224, 2483–2487, 2523 |
| `cardPadder` | 4 | 3 | 424, 1010, 3547–3551 |
| `cardText` | 4 | 3 | 924–934, 3556, 7167 |
| `detailPageContent` | 4 | 3 | 1762, 4697, 4970–4977 |
| `dialog-fullscreen` | 4 | 3 | 3390, 6793–6803, 6829 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7188, 7724 |
| `folder` | 4 | 3 | 1925–1930, 3657, 3721 |
| `formDialogFooter` | 4 | 3 | 3448, 3931, 7399–7423 |
| `infoWrapper` | 4 | 3 | 2167–2172, 2430, 2458 |
| `listItemImage` | 4 | 3 | 2801–2806, 4475, 7382 |
| `musicParentName` | 4 | 3 | 2001, 2536, 5610–5619 |
| `programGuideSection` | 4 | 3 | 2491–2506, 4866, 4893 |
| `toast` | 4 | 3 | 5144, 6793–6803, 6829 |
| `cardFooter` | 3 | 3 | 3567, 6897, 6932 |
| `collectionItems` | 3 | 3 | 1772, 4866, 4902 |
| `defaultCardBackground` | 3 | 3 | 3678, 6117, 6216 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `emby-input` | 3 | 3 | 5404, 5433, 7465 |
| `formDialogFooterItem` | 3 | 3 | 3448, 3716, 3842 |
| `formDialogHeader` | 3 | 3 | 3931, 7347, 7399 |
| `iconOsd` | 3 | 3 | 5897, 7347, 7399 |
| `live_tv` | 3 | 3 | 2001, 2523, 3965 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4675, 4991 |
| `page` | 3 | 3 | 1006, 2698, 6849 |
| `playerStats` | 3 | 3 | 5897, 7399, 7435 |
| `sectionTitle-cards` | 3 | 3 | 1740, 5060, 5120 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4902 |
| `tsx` | 3 | 3 | 1084, 4373, 4450 |
| `itemExternalLinks` | 13 | 2 | 3100–3178, 3330 |
| `checkboxOutline` | 10 | 2 | 3501–3542, 3573–3603 |
| `itemBackdrop` | 9 | 2 | 1967–2022, 2197 |
| `mdl-slider` | 9 | 2 | 2897, 2952–3010 |
| `listItemIcon` | 8 | 2 | 3961–3965, 4615–4675 |
| `sliderContainer` | 8 | 2 | 2901, 2929–2994 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3266–3292, 3318–3322 |
| `divUsers` | 7 | 2 | 5998–6002, 7151–7178 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3538–3542, 3572–3591 |
| `countIndicator` | 6 | 2 | 767–797, 7399–7423 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2430 |
| `detailsGroupItem` | 6 | 2 | 4728, 4796–4833 |
| `headerButton` | 6 | 2 | 557–637, 6478 |
| `headerLeft` | 6 | 2 | 1690–1727, 6686 |
| `selectionCommandsPanel` | 6 | 2 | 3458–3492, 7347 |
| `trackSelections` | 6 | 2 | 4701–4728, 4861–4866 |
| `withBackdrop` | 6 | 2 | 2606, 2648–2666 |
| `detailSection` | 5 | 2 | 4684–4693, 4846–4866 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7399–7423 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3060, 7064–7081 |
| `mediaInfoItem` | 5 | 2 | 1844–1887, 6941 |
| `overview-expand` | 5 | 2 | 3298–3322, 4766 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3646–3674, 7399 |
| `withSectionTabs` | 5 | 2 | 2657–2674, 6361 |
| `alphaPickerButton` | 4 | 2 | 637, 4917–4929 |
| `backgroundProgress` | 4 | 2 | 2812–2824, 2854 |
| `emby-select` | 4 | 2 | 5404–5416, 7465 |
| `emby-tab-button-active` | 4 | 2 | 3903, 6568–6582 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7399 |
| `play_arrow` | 4 | 2 | 3683–3699, 3870 |
| `playbackProgress` | 4 | 2 | 2812–2824, 2859 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4502–4507, 6210–6216 |
| `programCell` | 4 | 2 | 5660, 5719–5728 |
| `section0` | 4 | 2 | 976–1006, 6849 |
| `visualLoginForm` | 4 | 2 | 5989–6006, 6047 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3542–3551 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7731–7738 |
| `emby-textarea` | 3 | 2 | 5395–5404, 5433 |
| `guestCastContent` | 3 | 2 | 833, 3542–3551 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5694–5710 |
| `guide-date-tab-button` | 3 | 2 | 637, 3903–3911 |
| `headerUserButton` | 3 | 2 | 557–570, 4995 |
| `manualLoginForm` | 3 | 2 | 5989–6006, 6047 |
| `overview` | 3 | 2 | 3318–3322, 4776 |
| `add` | 2 | 2 | 1745, 6941 |
| `alphaPicker-fixed-right` | 2 | 2 | 2698, 4929 |
| `backdropImageFadeIn` | 2 | 2 | 2751, 7439 |
| `book` | 2 | 2 | 2001, 2523 |
| `btnDeleteImage` | 2 | 2 | 3703, 3917 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 5090, 5134 |
| `classList` | 2 | 2 | 1745, 6941 |
| `collapseContent` | 2 | 2 | 3453, 3929 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4906 |
| `content-primary` | 2 | 2 | 4970, 5026 |
| `editorsChoiceItemOverview` | 2 | 2 | 7661, 7742 |
| `endsAt` | 2 | 2 | 1865, 6941 |
| `fieldDescription` | 2 | 2 | 302, 7465 |
| `formDialogFooter-clear` | 2 | 2 | 3448, 3931 |
| `guide-programNameCaret` | 2 | 2 | 302, 5676 |
| `headroom` | 2 | 2 | 6349, 6386 |
| `indicator` | 2 | 2 | 797, 3635 |
| `mediaInfoOfficialRating` | 2 | 2 | 1865, 6941 |
| `navMenuOption-selected` | 2 | 2 | 4680, 7075 |
| `nowPlayingInfoContainer` | 2 | 2 | 3091, 6147 |
| `org` | 2 | 2 | 3127, 3157 |
| `paperList` | 2 | 2 | 842, 3942 |
| `playlist` | 2 | 2 | 4497, 6125 |
| `programSecondaryTitle` | 2 | 2 | 302, 5728 |
| `queue` | 2 | 2 | 2001, 2523 |
| `reactRoot` | 2 | 2 | 4373, 6692 |
| `readOnlyContent` | 2 | 2 | 3973, 6615 |
| `recordingFields` | 2 | 2 | 4720, 4861 |
| `runtime` | 2 | 2 | 6059, 6087 |
| `sectionTitleContainer-cards` | 2 | 2 | 5055, 5120 |
| `sidebarHeader` | 2 | 2 | 4065, 7081 |
| `tagline` | 2 | 2 | 2597, 4776 |
| `upNextDialog-title` | 2 | 2 | 5176, 5210 |
| `vertical-list` | 2 | 2 | 1807, 7567 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3083, 6316 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3083, 6316 |
| `userPreferencesPage` | 12 | 1 | 7450–7546 |
| `checkboxContainer` | 7 | 1 | 3530–3567 |
| `itemDetailsGroup` | 7 | 1 | 4780–4866 |
| `itemProgressBar` | 6 | 1 | 2801–2835 |
| `streaming-lookup-container` | 6 | 1 | 3185–3230 |
| `trackSelectionFieldContainer` | 6 | 1 | 4739–4762 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7698–7738 |
| `innerCardFooter` | 5 | 1 | 3343–3372 |
| `chapterCardImageContainer` | 4 | 1 | 3343–3372 |
| `emby-select-withcolor` | 4 | 1 | 5404–5451 |
| `endTimeText` | 4 | 1 | 6059–6087 |
| `mainDetailButtons` | 4 | 1 | 3866–3880 |
| `overview-controls` | 4 | 1 | 3318–3330 |
| `startTimeText` | 4 | 1 | 6059–6081 |
| `button-flat` | 3 | 1 | 3064–3074 |
| `cardIndicators` | 3 | 1 | 3620–3630 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3133–3151 |
| `content` | 3 | 1 | 4802–4833 |
| `discover-card` | 3 | 1 | 7749–7772 |
| `fab` | 3 | 1 | 3725–3738 |
| `listChildrenCollapsible` | 3 | 1 | 4851–4866 |
| `mdl-slider-background-flex` | 3 | 1 | 2921–2934 |
| `mediaInfoCriticRating` | 3 | 1 | 1906–1915 |
| `nextUpSection` | 3 | 1 | 4846–4866 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6111–6121 |
| `serverInfo` | 3 | 1 | 3946–3955 |
| `transcodingProgress` | 3 | 1 | 2812–2824 |
