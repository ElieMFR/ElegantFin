# Index des composants — ElegantFin Cinema Edition v1.3.17

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.17.css` — 7623 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2127–2160, 2187–2191, 2467–2485, 2521, 6595, 6853–6869, 6947–6969, 6999–7006, 7096, 7501 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2485, 3490, 3601, 3680, 5783, 6609–6619, 6688, 6853, 6990–7006 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2000–2036, 2071–2086, 2122, 2223, 2534, 3935–3946, 4599, 4886, 7329–7367 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1886, 3447, 3606, 3680–3686, 3792, 3950, 4479, 4989, 5023–5033, 5601 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5908–5912, 5992, 6601, 6680–6688, 6728, 6853–6869, 6990 |
| `skinHeader` | 16 | 10 | 284, 4291, 4337–4364, 5791, 6201, 6257–6265, 6291–6316, 6671, 6820, 7438 |
| `nameContainer` | 27 | 9 | 694, 2230–2253, 2294, 2323, 2358–2404, 2441, 2472–2476, 5358–5410, 7329–7367 |
| `js` | 9 | 9 | 331, 1652, 1745, 2294, 2898, 3580, 5601, 6772, 7016 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5912, 6619, 6728–6763, 6853, 7142 |
| `parentName` | 23 | 8 | 694, 2235–2253, 2294, 2323, 2358–2404, 5364–5410, 5483, 7329–7367 |
| `detailLogo` | 20 | 8 | 694, 2010–2036, 2071–2086, 2113–2122, 2223–2253, 2323, 2358–2404, 2472 |
| `listItem` | 19 | 8 | 302, 637, 2489, 4399–4425, 4456–4488, 4533, 4574, 7119–7136 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2036, 2196, 2230–2253, 2323, 2358–2404, 2472 |
| `subtitle` | 16 | 8 | 2000–2010, 2122, 2235, 2294, 2413–2423, 2534, 5418–5451, 7329–7367 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2000–2010, 2139, 2223, 2476–2485, 2512, 2821 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6595, 6853, 7142 |
| `emby-button` | 11 | 8 | 620–637, 664–682, 3160, 3221–3228, 3626, 3661, 3814, 4497 |
| `nowPlayingBar` | 8 | 8 | 318, 3084, 6044, 6634, 6722, 6806, 6832, 7101 |
| `loginPage` | 16 | 7 | 3759, 5795–5826, 5865, 5893–5912, 6624, 6667, 6979–7006 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4000, 4466–4488, 4580–4585, 6892–6903 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3387–3407, 5277 |
| `verticalSection` | 11 | 6 | 1740, 2723–2728, 4886, 6680, 6772, 7016 |
| `button-link` | 10 | 6 | 637, 664–682, 3034–3043, 3104–3114, 3160, 7292 |
| `person` | 8 | 6 | 2000–2021, 2223, 2476, 2521–2530, 3887, 7324 |
| `mainDrawer` | 7 | 6 | 3048, 3964, 4337, 6624–6634, 6879, 6918 |
| `detailImageContainer` | 20 | 5 | 2000–2021, 2127–2191, 2223, 2463–2485, 2512–2530 |
| `osdHeader` | 15 | 5 | 1709–1727, 6196–6265, 6291–6316, 6671, 7101 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4399–4410, 4456, 4533–4574, 6652 |
| `sectionTabs` | 10 | 5 | 1803, 3738, 4364, 6237–6242, 6382–6413 |
| `cardImageIcon` | 8 | 5 | 420–424, 2476–2485, 2548, 3474, 5992 |
| `headerTop` | 8 | 5 | 4291, 4337, 6207–6232, 6283–6300, 6327–6331 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4192, 4959–4967, 5860 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2713, 6680, 6772 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1924–1929, 2187, 2821 |
| `scss` | 5 | 5 | 284, 776, 1036, 3496, 6772 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 3935, 5791, 6196, 6246 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3690–3732, 3765–3792 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7101–7119 |
| `itemName` | 11 | 4 | 694, 2294, 5364–5410, 5501–5518 |
| `backdropImage` | 10 | 4 | 2613–2640, 2667–2671, 6588, 6688–6696 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3738, 6367–6408 |
| `upNextContainer` | 10 | 4 | 5051–5070, 5096–5122, 6624–6634, 6660 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 6922–6969, 7080–7096 |
| `backgroundContainer` | 8 | 4 | 2090, 2604, 2645–2663, 2695 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1839, 1924–1936, 7324 |
| `listItemBodyText` | 7 | 4 | 4420–4439, 4479, 4554, 7136 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3759, 3846, 5893–5901, 7204–7218 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3479–3483, 6750–6758 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2428, 4880, 6836 |
| `skip-button` | 6 | 4 | 637, 3743, 5145–5162, 5189–5195 |
| `squareCard` | 6 | 4 | 865, 2476, 2512–2530, 5869–5873 |
| `skinHeader-blurred` | 5 | 4 | 5791, 6225–6232, 6820, 7101 |
| `appfooter` | 4 | 4 | 2764, 6341, 6711, 7101 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4886 |
| `raised` | 4 | 4 | 637, 723, 3626, 3661 |
| `detailButton` | 13 | 3 | 582–637, 3671–3732, 3788–3792 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3419, 3447–3490 |
| `pageTitle` | 8 | 3 | 1684–1727, 6257, 6316 |
| `sectionTitleTextButton` | 8 | 3 | 4942–4950, 4977–4989, 5023–5033 |
| `homePage` | 7 | 3 | 4291, 4337–4364, 6430 |
| `playedIndicator` | 7 | 3 | 776–790, 3563, 6853–6874 |
| `check` | 6 | 3 | 3447, 3680, 4533–4574 |
| `detailSectionContent` | 6 | 3 | 3253, 4681–4691, 4771–4781 |
| `emby-checkbox` | 6 | 3 | 3424, 3461–3465, 3514–3526 |
| `actionSheetContent` | 5 | 3 | 4525–4529, 6624–6634, 6660 |
| `cardText-first` | 5 | 3 | 924, 3453–3479, 5973 |
| `dialog` | 5 | 3 | 3303–3313, 6624–6634, 6660 |
| `guideProgramName` | 5 | 3 | 637, 5542–5553, 5596–5601 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6257, 6367–6375 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3457, 5968–5973 |
| `secondary` | 5 | 3 | 302, 4429–4439, 4479 |
| `album` | 4 | 3 | 2223, 2481–2485, 2521 |
| `cardPadder` | 4 | 3 | 424, 1010, 3470–3474 |
| `cardText` | 4 | 3 | 924–934, 3479, 6995 |
| `detailPageContent` | 4 | 3 | 1762, 4612, 4873–4880 |
| `dialog-fullscreen` | 4 | 3 | 3313, 6624–6634, 6660 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7016, 7476 |
| `folder` | 4 | 3 | 1924–1929, 3580, 3644 |
| `formDialogFooter` | 4 | 3 | 3371, 3853, 7153–7177 |
| `infoWrapper` | 4 | 3 | 2166–2171, 2428, 2456 |
| `listItemImage` | 4 | 3 | 2798–2803, 4393, 7136 |
| `musicParentName` | 4 | 3 | 2000, 2534, 5483–5492 |
| `semiTransparent` | 4 | 3 | 1648, 5791, 6225–6246 |
| `toast` | 4 | 3 | 5043, 6624–6634, 6660 |
| `cardFooter` | 3 | 3 | 3490, 6728, 6763 |
| `defaultCardBackground` | 3 | 3 | 3601, 5988, 6087 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `formDialogFooterItem` | 3 | 3 | 3371, 3639, 3765 |
| `formDialogHeader` | 3 | 3 | 3853, 7101, 7153 |
| `iconOsd` | 3 | 3 | 5769, 7101, 7153 |
| `live_tv` | 3 | 3 | 2000, 2521, 3887 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4590, 4894 |
| `page` | 3 | 3 | 1006, 2695, 6680 |
| `playerStats` | 3 | 3 | 5769, 7153, 7189 |
| `sectionTitle-cards` | 3 | 3 | 1740, 4959, 5019 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4805 |
| `tsx` | 3 | 3 | 1084, 4291, 4368 |
| `x` | 3 | 3 | 2294, 5466, 6772 |
| `itemExternalLinks` | 13 | 2 | 3097–3175, 3253 |
| `checkboxOutline` | 10 | 2 | 3424–3465, 3496–3526 |
| `itemBackdrop` | 9 | 2 | 1966–2021, 2196 |
| `mdl-slider` | 9 | 2 | 2894, 2949–3007 |
| `listItemIcon` | 8 | 2 | 3883–3887, 4533–4590 |
| `sliderContainer` | 8 | 2 | 2898, 2926–2991 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3189–3215, 3241–3245 |
| `divUsers` | 7 | 2 | 5869–5873, 6979–7006 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3461–3465, 3495–3514 |
| `countIndicator` | 6 | 2 | 767–797, 7153–7177 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2428 |
| `detailsGroupItem` | 6 | 2 | 4643, 4711–4748 |
| `headerButton` | 6 | 2 | 557–637, 6309 |
| `headerLeft` | 6 | 2 | 1690–1727, 6517 |
| `selectionCommandsPanel` | 6 | 2 | 3381–3415, 7101 |
| `trackSelections` | 6 | 2 | 4616–4643, 4776–4781 |
| `withBackdrop` | 6 | 2 | 2604, 2645–2663 |
| `detailSection` | 5 | 2 | 4599–4608, 4761–4781 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7153–7177 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3057, 6892–6909 |
| `mediaInfoItem` | 5 | 2 | 1843–1886, 6772 |
| `overview-expand` | 5 | 2 | 3221–3245, 4681 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3569–3597, 7153 |
| `withSectionTabs` | 5 | 2 | 2654–2671, 6232 |
| `alphaPickerButton` | 4 | 2 | 637, 4820–4832 |
| `backgroundProgress` | 4 | 2 | 2809–2821, 2851 |
| `emby-tab-button-active` | 4 | 2 | 3825, 6399–6413 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7153 |
| `play_arrow` | 4 | 2 | 3606–3622, 3792 |
| `playbackProgress` | 4 | 2 | 2809–2821, 2856 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4420–4425, 6081–6087 |
| `programCell` | 4 | 2 | 5533, 5592–5601 |
| `programGuideSection` | 4 | 2 | 2489–2504, 4781–4796 |
| `section0` | 4 | 2 | 976–1006, 6680 |
| `visualLoginForm` | 4 | 2 | 5860–5877, 5918 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3465–3474 |
| `collectionItems` | 3 | 2 | 1772, 4781–4805 |
| `emby-input` | 3 | 2 | 5291–5307, 7218 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7483–7490 |
| `guestCastContent` | 3 | 2 | 833, 3465–3474 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5567–5583 |
| `guide-date-tab-button` | 3 | 2 | 637, 3825–3833 |
| `headerUserButton` | 3 | 2 | 557–570, 4898 |
| `manualLoginForm` | 3 | 2 | 5860–5877, 5918 |
| `overview` | 3 | 2 | 3241–3245, 4691 |
| `add` | 2 | 2 | 1745, 6772 |
| `alphaPicker-fixed-right` | 2 | 2 | 2695, 4832 |
| `backdropImageFadeIn` | 2 | 2 | 2748, 7193 |
| `book` | 2 | 2 | 2000, 2521 |
| `btnDeleteImage` | 2 | 2 | 3626, 3839 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 4989, 5033 |
| `classList` | 2 | 2 | 1745, 6772 |
| `collapseContent` | 2 | 2 | 3376, 3851 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4809 |
| `content-primary` | 2 | 2 | 4873, 4925 |
| `editorsChoiceItemOverview` | 2 | 2 | 7413, 7494 |
| `emby-select` | 2 | 2 | 5291, 7218 |
| `endsAt` | 2 | 2 | 1864, 6772 |
| `fieldDescription` | 2 | 2 | 302, 7218 |
| `formDialogFooter-clear` | 2 | 2 | 3371, 3853 |
| `guide-programNameCaret` | 2 | 2 | 302, 5549 |
| `headroom` | 2 | 2 | 6220, 6257 |
| `indicator` | 2 | 2 | 797, 3558 |
| `mediaInfoOfficialRating` | 2 | 2 | 1864, 6772 |
| `navMenuOption-selected` | 2 | 2 | 4595, 6903 |
| `nowPlayingInfoContainer` | 2 | 2 | 3088, 6018 |
| `org` | 2 | 2 | 3124, 3154 |
| `paperList` | 2 | 2 | 842, 3864 |
| `playlist` | 2 | 2 | 4415, 5996 |
| `programSecondaryTitle` | 2 | 2 | 302, 5601 |
| `queue` | 2 | 2 | 2000, 2521 |
| `reactRoot` | 2 | 2 | 4291, 6523 |
| `readOnlyContent` | 2 | 2 | 3895, 6446 |
| `recordingFields` | 2 | 2 | 4635, 4776 |
| `runtime` | 2 | 2 | 5930, 5958 |
| `sectionTitleContainer-cards` | 2 | 2 | 4954, 5019 |
| `sidebarHeader` | 2 | 2 | 3987, 6909 |
| `tagline` | 2 | 2 | 2595, 4691 |
| `upNextDialog-title` | 2 | 2 | 5075, 5109 |
| `vertical-list` | 2 | 2 | 1807, 7319 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3080, 6187 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3080, 6187 |
| `userPreferencesPage` | 12 | 1 | 7204–7299 |
| `checkboxContainer` | 7 | 1 | 3453–3490 |
| `itemDetailsGroup` | 7 | 1 | 4695–4781 |
| `itemProgressBar` | 6 | 1 | 2798–2832 |
| `trackSelectionFieldContainer` | 6 | 1 | 4654–4677 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7450–7490 |
| `innerCardFooter` | 5 | 1 | 3266–3295 |
| `chapterCardImageContainer` | 4 | 1 | 3266–3295 |
| `endTimeText` | 4 | 1 | 5930–5958 |
| `mainDetailButtons` | 4 | 1 | 3788–3802 |
| `overview-controls` | 4 | 1 | 3241–3253 |
| `startTimeText` | 4 | 1 | 5930–5952 |
| `button-flat` | 3 | 1 | 3061–3071 |
| `cardIndicators` | 3 | 1 | 3543–3553 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3130–3148 |
| `content` | 3 | 1 | 4717–4748 |
| `discover-card` | 3 | 1 | 7501–7524 |
| `emby-select-withcolor` | 3 | 1 | 5291–5325 |
| `emby-textarea` | 3 | 1 | 5282–5307 |
| `fab` | 3 | 1 | 3648–3661 |
| `listChildrenCollapsible` | 3 | 1 | 4766–4781 |
| `mdl-slider-background-flex` | 3 | 1 | 2918–2931 |
| `mediaInfoCriticRating` | 3 | 1 | 1905–1914 |
| `nextUpSection` | 3 | 1 | 4761–4781 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5982–5992 |
| `serverInfo` | 3 | 1 | 3868–3877 |
| `transcodingProgress` | 3 | 1 | 2809–2821 |
