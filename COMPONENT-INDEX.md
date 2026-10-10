# Index des composants — ElegantFin Cinema Edition v1.3.18

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.18.css` — 7639 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2127–2160, 2187–2191, 2467–2485, 2521, 6611, 6869–6885, 6963–6985, 7015–7022, 7112, 7517 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2485, 3490, 3601, 3680, 5799, 6625–6635, 6704, 6869, 7006–7022 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2000–2036, 2071–2086, 2122, 2223, 2534, 3935–3946, 4603, 4890, 7345–7383 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1886, 3447, 3606, 3680–3686, 3792, 3950, 4483, 4993, 5027–5037, 5617 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5924–5928, 6008, 6617, 6696–6704, 6744, 6869–6885, 7006 |
| `skinHeader` | 16 | 10 | 284, 4295, 4341–4368, 5807, 6217, 6273–6281, 6307–6332, 6687, 6836, 7454 |
| `nameContainer` | 27 | 9 | 694, 2230–2253, 2294, 2323, 2358–2404, 2441, 2472–2476, 5374–5426, 7345–7383 |
| `emby-button` | 12 | 9 | 620–637, 664–682, 3160, 3221–3228, 3626, 3661, 3814, 4501, 5209 |
| `js` | 9 | 9 | 331, 1652, 1745, 2294, 2898, 3580, 5617, 6788, 7032 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5928, 6635, 6744–6779, 6869, 7158 |
| `parentName` | 23 | 8 | 694, 2235–2253, 2294, 2323, 2358–2404, 5380–5426, 5499, 7345–7383 |
| `detailLogo` | 20 | 8 | 694, 2010–2036, 2071–2086, 2113–2122, 2223–2253, 2323, 2358–2404, 2472 |
| `listItem` | 19 | 8 | 302, 637, 2489, 4403–4429, 4460–4492, 4537, 4578, 7135–7152 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2036, 2196, 2230–2253, 2323, 2358–2404, 2472 |
| `subtitle` | 16 | 8 | 2000–2010, 2122, 2235, 2294, 2413–2423, 2534, 5434–5467, 7345–7383 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2000–2010, 2139, 2223, 2476–2485, 2512, 2821 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6611, 6869, 7158 |
| `nowPlayingBar` | 8 | 8 | 318, 3084, 6060, 6650, 6738, 6822, 6848, 7117 |
| `loginPage` | 16 | 7 | 3759, 5811–5842, 5881, 5909–5928, 6640, 6683, 6995–7022 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4000, 4470–4492, 4584–4589, 6908–6919 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3387–3407, 5293 |
| `verticalSection` | 11 | 6 | 1740, 2723–2728, 4890, 6696, 6788, 7032 |
| `button-link` | 10 | 6 | 637, 664–682, 3034–3043, 3104–3114, 3160, 7308 |
| `person` | 8 | 6 | 2000–2021, 2223, 2476, 2521–2530, 3887, 7340 |
| `mainDrawer` | 7 | 6 | 3048, 3964, 4341, 6640–6650, 6895, 6934 |
| `scss` | 6 | 6 | 284, 776, 1036, 3496, 4006, 6788 |
| `detailImageContainer` | 20 | 5 | 2000–2021, 2127–2191, 2223, 2463–2485, 2512–2530 |
| `osdHeader` | 15 | 5 | 1709–1727, 6212–6281, 6307–6332, 6687, 7117 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4403–4414, 4460, 4537–4578, 6668 |
| `sectionTabs` | 10 | 5 | 1803, 3738, 4368, 6253–6258, 6398–6429 |
| `cardImageIcon` | 8 | 5 | 420–424, 2476–2485, 2548, 3474, 6008 |
| `headerTop` | 8 | 5 | 4295, 4341, 6223–6248, 6299–6316, 6343–6347 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4196, 4963–4971, 5876 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2713, 6696, 6788 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1924–1929, 2187, 2821 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 3935, 5807, 6212, 6262 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3690–3732, 3765–3792 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7117–7135 |
| `itemName` | 11 | 4 | 694, 2294, 5380–5426, 5517–5534 |
| `backdropImage` | 10 | 4 | 2613–2640, 2667–2671, 6604, 6704–6712 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3738, 6383–6424 |
| `upNextContainer` | 10 | 4 | 5055–5074, 5100–5126, 6640–6650, 6676 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 6938–6985, 7096–7112 |
| `backgroundContainer` | 8 | 4 | 2090, 2604, 2645–2663, 2695 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1839, 1924–1936, 7340 |
| `listItemBodyText` | 7 | 4 | 4424–4443, 4483, 4558, 7152 |
| `skip-button` | 7 | 4 | 637, 3743, 5149–5166, 5193–5211 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3759, 3846, 5909–5917, 7220–7234 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3479–3483, 6766–6774 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2428, 4884, 6852 |
| `squareCard` | 6 | 4 | 865, 2476, 2512–2530, 5885–5889 |
| `skinHeader-blurred` | 5 | 4 | 5807, 6241–6248, 6836, 7117 |
| `appfooter` | 4 | 4 | 2764, 6357, 6727, 7117 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4890 |
| `raised` | 4 | 4 | 637, 723, 3626, 3661 |
| `x` | 4 | 4 | 2294, 4006, 5482, 6788 |
| `detailButton` | 13 | 3 | 582–637, 3671–3732, 3788–3792 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3419, 3447–3490 |
| `pageTitle` | 8 | 3 | 1684–1727, 6273, 6332 |
| `sectionTitleTextButton` | 8 | 3 | 4946–4954, 4981–4993, 5027–5037 |
| `homePage` | 7 | 3 | 4295, 4341–4368, 6446 |
| `playedIndicator` | 7 | 3 | 776–790, 3563, 6869–6890 |
| `check` | 6 | 3 | 3447, 3680, 4537–4578 |
| `detailSectionContent` | 6 | 3 | 3253, 4685–4695, 4775–4785 |
| `emby-checkbox` | 6 | 3 | 3424, 3461–3465, 3514–3526 |
| `actionSheetContent` | 5 | 3 | 4529–4533, 6640–6650, 6676 |
| `cardText-first` | 5 | 3 | 924, 3453–3479, 5989 |
| `dialog` | 5 | 3 | 3303–3313, 6640–6650, 6676 |
| `guideProgramName` | 5 | 3 | 637, 5558–5569, 5612–5617 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6273, 6383–6391 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3457, 5984–5989 |
| `secondary` | 5 | 3 | 302, 4433–4443, 4483 |
| `album` | 4 | 3 | 2223, 2481–2485, 2521 |
| `cardPadder` | 4 | 3 | 424, 1010, 3470–3474 |
| `cardText` | 4 | 3 | 924–934, 3479, 7011 |
| `detailPageContent` | 4 | 3 | 1762, 4616, 4877–4884 |
| `dialog-fullscreen` | 4 | 3 | 3313, 6640–6650, 6676 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7032, 7492 |
| `folder` | 4 | 3 | 1924–1929, 3580, 3644 |
| `formDialogFooter` | 4 | 3 | 3371, 3853, 7169–7193 |
| `infoWrapper` | 4 | 3 | 2166–2171, 2428, 2456 |
| `listItemImage` | 4 | 3 | 2798–2803, 4397, 7152 |
| `musicParentName` | 4 | 3 | 2000, 2534, 5499–5508 |
| `semiTransparent` | 4 | 3 | 1648, 5807, 6241–6262 |
| `toast` | 4 | 3 | 5047, 6640–6650, 6676 |
| `cardFooter` | 3 | 3 | 3490, 6744, 6779 |
| `defaultCardBackground` | 3 | 3 | 3601, 6004, 6103 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `formDialogFooterItem` | 3 | 3 | 3371, 3639, 3765 |
| `formDialogHeader` | 3 | 3 | 3853, 7117, 7169 |
| `iconOsd` | 3 | 3 | 5785, 7117, 7169 |
| `live_tv` | 3 | 3 | 2000, 2521, 3887 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4594, 4898 |
| `page` | 3 | 3 | 1006, 2695, 6696 |
| `playerStats` | 3 | 3 | 5785, 7169, 7205 |
| `sectionTitle-cards` | 3 | 3 | 1740, 4963, 5023 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4809 |
| `tsx` | 3 | 3 | 1084, 4295, 4372 |
| `itemExternalLinks` | 13 | 2 | 3097–3175, 3253 |
| `checkboxOutline` | 10 | 2 | 3424–3465, 3496–3526 |
| `itemBackdrop` | 9 | 2 | 1966–2021, 2196 |
| `mdl-slider` | 9 | 2 | 2894, 2949–3007 |
| `listItemIcon` | 8 | 2 | 3883–3887, 4537–4594 |
| `sliderContainer` | 8 | 2 | 2898, 2926–2991 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3189–3215, 3241–3245 |
| `divUsers` | 7 | 2 | 5885–5889, 6995–7022 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3461–3465, 3495–3514 |
| `countIndicator` | 6 | 2 | 767–797, 7169–7193 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2428 |
| `detailsGroupItem` | 6 | 2 | 4647, 4715–4752 |
| `headerButton` | 6 | 2 | 557–637, 6325 |
| `headerLeft` | 6 | 2 | 1690–1727, 6533 |
| `selectionCommandsPanel` | 6 | 2 | 3381–3415, 7117 |
| `trackSelections` | 6 | 2 | 4620–4647, 4780–4785 |
| `withBackdrop` | 6 | 2 | 2604, 2645–2663 |
| `detailSection` | 5 | 2 | 4603–4612, 4765–4785 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7169–7193 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3057, 6908–6925 |
| `mediaInfoItem` | 5 | 2 | 1843–1886, 6788 |
| `overview-expand` | 5 | 2 | 3221–3245, 4685 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3569–3597, 7169 |
| `withSectionTabs` | 5 | 2 | 2654–2671, 6248 |
| `alphaPickerButton` | 4 | 2 | 637, 4824–4836 |
| `backgroundProgress` | 4 | 2 | 2809–2821, 2851 |
| `emby-tab-button-active` | 4 | 2 | 3825, 6415–6429 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7169 |
| `play_arrow` | 4 | 2 | 3606–3622, 3792 |
| `playbackProgress` | 4 | 2 | 2809–2821, 2856 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4424–4429, 6097–6103 |
| `programCell` | 4 | 2 | 5549, 5608–5617 |
| `programGuideSection` | 4 | 2 | 2489–2504, 4785–4800 |
| `section0` | 4 | 2 | 976–1006, 6696 |
| `visualLoginForm` | 4 | 2 | 5876–5893, 5934 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3465–3474 |
| `collectionItems` | 3 | 2 | 1772, 4785–4809 |
| `emby-input` | 3 | 2 | 5307–5323, 7234 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7499–7506 |
| `guestCastContent` | 3 | 2 | 833, 3465–3474 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5583–5599 |
| `guide-date-tab-button` | 3 | 2 | 637, 3825–3833 |
| `headerUserButton` | 3 | 2 | 557–570, 4902 |
| `manualLoginForm` | 3 | 2 | 5876–5893, 5934 |
| `overview` | 3 | 2 | 3241–3245, 4695 |
| `add` | 2 | 2 | 1745, 6788 |
| `alphaPicker-fixed-right` | 2 | 2 | 2695, 4836 |
| `backdropImageFadeIn` | 2 | 2 | 2748, 7209 |
| `book` | 2 | 2 | 2000, 2521 |
| `btnDeleteImage` | 2 | 2 | 3626, 3839 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 4993, 5037 |
| `classList` | 2 | 2 | 1745, 6788 |
| `collapseContent` | 2 | 2 | 3376, 3851 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4813 |
| `content-primary` | 2 | 2 | 4877, 4929 |
| `editorsChoiceItemOverview` | 2 | 2 | 7429, 7510 |
| `emby-select` | 2 | 2 | 5307, 7234 |
| `endsAt` | 2 | 2 | 1864, 6788 |
| `fieldDescription` | 2 | 2 | 302, 7234 |
| `formDialogFooter-clear` | 2 | 2 | 3371, 3853 |
| `guide-programNameCaret` | 2 | 2 | 302, 5565 |
| `headroom` | 2 | 2 | 6236, 6273 |
| `indicator` | 2 | 2 | 797, 3558 |
| `mediaInfoOfficialRating` | 2 | 2 | 1864, 6788 |
| `navMenuOption-selected` | 2 | 2 | 4599, 6919 |
| `nowPlayingInfoContainer` | 2 | 2 | 3088, 6034 |
| `org` | 2 | 2 | 3124, 3154 |
| `paperList` | 2 | 2 | 842, 3864 |
| `playlist` | 2 | 2 | 4419, 6012 |
| `programSecondaryTitle` | 2 | 2 | 302, 5617 |
| `queue` | 2 | 2 | 2000, 2521 |
| `reactRoot` | 2 | 2 | 4295, 6539 |
| `readOnlyContent` | 2 | 2 | 3895, 6462 |
| `recordingFields` | 2 | 2 | 4639, 4780 |
| `runtime` | 2 | 2 | 5946, 5974 |
| `sectionTitleContainer-cards` | 2 | 2 | 4958, 5023 |
| `sidebarHeader` | 2 | 2 | 3987, 6925 |
| `tagline` | 2 | 2 | 2595, 4695 |
| `upNextDialog-title` | 2 | 2 | 5079, 5113 |
| `vertical-list` | 2 | 2 | 1807, 7335 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3080, 6203 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3080, 6203 |
| `userPreferencesPage` | 12 | 1 | 7220–7315 |
| `checkboxContainer` | 7 | 1 | 3453–3490 |
| `itemDetailsGroup` | 7 | 1 | 4699–4785 |
| `itemProgressBar` | 6 | 1 | 2798–2832 |
| `trackSelectionFieldContainer` | 6 | 1 | 4658–4681 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7466–7506 |
| `innerCardFooter` | 5 | 1 | 3266–3295 |
| `chapterCardImageContainer` | 4 | 1 | 3266–3295 |
| `endTimeText` | 4 | 1 | 5946–5974 |
| `mainDetailButtons` | 4 | 1 | 3788–3802 |
| `overview-controls` | 4 | 1 | 3241–3253 |
| `startTimeText` | 4 | 1 | 5946–5968 |
| `button-flat` | 3 | 1 | 3061–3071 |
| `cardIndicators` | 3 | 1 | 3543–3553 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3130–3148 |
| `content` | 3 | 1 | 4721–4752 |
| `discover-card` | 3 | 1 | 7517–7540 |
| `emby-select-withcolor` | 3 | 1 | 5307–5341 |
| `emby-textarea` | 3 | 1 | 5298–5323 |
| `fab` | 3 | 1 | 3648–3661 |
| `listChildrenCollapsible` | 3 | 1 | 4770–4785 |
| `mdl-slider-background-flex` | 3 | 1 | 2918–2931 |
| `mediaInfoCriticRating` | 3 | 1 | 1905–1914 |
| `nextUpSection` | 3 | 1 | 4765–4785 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5998–6008 |
| `serverInfo` | 3 | 1 | 3868–3877 |
| `transcodingProgress` | 3 | 1 | 2809–2821 |
