# Index des composants — ElegantFin Cinema Edition v1.3.13

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.13.css` — 7420 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 420–502, 740, 857, 1503–1523, 2090–2123, 2150–2154, 2430–2448, 2484, 6392, 6650–6666, 6744–6766, 6796–6803, 6893, 7298 |
| `cardScalable` | 28 | 13 | 420–431, 479–502, 803–847, 873–911, 2448, 3453, 3564, 3643, 5585, 6406–6416, 6485, 6650, 6787–6803 |
| `material-icons` | 17 | 13 | 356–375, 1722, 1820, 1872, 3410, 3569, 3643–3649, 3755, 3913, 4303, 4787, 4821–4831, 5403 |
| `cardImageContainer` | 22 | 12 | 474, 825, 853–882, 911, 968–998, 5710–5714, 5794, 6398, 6477–6485, 6525, 6650–6666, 6787 |
| `itemDetailPage` | 21 | 12 | 1566, 1652, 1731, 1758, 1986–2022, 2057–2085, 2186, 2497, 3898–3909, 4397, 4684, 7126–7164 |
| `skinHeader` | 16 | 10 | 284, 4128, 4161–4188, 5593, 6003, 6059–6067, 6093–6118, 6468, 6617, 7235 |
| `nameContainer` | 27 | 9 | 686, 2193–2216, 2257, 2286, 2321–2367, 2404, 2435–2439, 5160–5212, 7126–7164 |
| `js` | 9 | 9 | 323, 1638, 1731, 2257, 2861, 3543, 5403, 6569, 6813 |
| `card-hoverable` | 23 | 8 | 502, 813, 873–961, 5714, 6416, 6525–6560, 6650, 6939 |
| `parentName` | 23 | 8 | 686, 2198–2216, 2257, 2286, 2321–2367, 5166–5212, 5285, 7126–7164 |
| `detailPageWrapperContainer` | 17 | 8 | 686, 1534–1544, 2022, 2159, 2193–2216, 2286, 2321–2367, 2435 |
| `subtitle` | 16 | 8 | 1986–1996, 2085, 2198, 2257, 2376–2386, 2497, 5220–5253, 7126–7164 |
| `backdropCard` | 12 | 8 | 955–961, 1076, 1986–1996, 2102, 2186, 2439–2448, 2475, 2784 |
| `cardBox` | 12 | 8 | 420–468, 494, 740, 895, 1002, 6392, 6650, 6939 |
| `emby-button` | 11 | 8 | 612–629, 656–674, 3123, 3184–3191, 3589, 3624, 3777, 4321 |
| `detailLogo` | 20 | 7 | 686, 1996–2022, 2057–2085, 2186–2216, 2286, 2321–2367, 2435 |
| `loginPage` | 16 | 7 | 3722, 5597–5628, 5667, 5695–5714, 6421, 6464, 6776–6803 |
| `nowPlayingBar` | 7 | 7 | 3047, 5846, 6431, 6519, 6603, 6629, 6898 |
| `listItem` | 17 | 6 | 302, 629, 2452, 4223–4249, 4280–4312, 6916–6933 |
| `navMenuOption` | 12 | 6 | 629, 725–735, 3963, 4290–4312, 4378–4383, 6689–6700 |
| `paper-icon-button-light` | 11 | 6 | 574–629, 1652, 1722, 1820, 3350–3370, 5079 |
| `verticalSection` | 11 | 6 | 1726, 2686–2691, 4684, 6477, 6569, 6813 |
| `button-link` | 10 | 6 | 629, 656–674, 2997–3006, 3067–3077, 3123, 7089 |
| `person` | 8 | 6 | 1986–2007, 2186, 2439, 2484–2493, 3850, 7121 |
| `mainDrawer` | 7 | 6 | 3011, 3927, 4161, 6421–6431, 6676, 6715 |
| `detailImageContainer` | 20 | 5 | 1986–2007, 2090–2154, 2186, 2426–2448, 2475–2493 |
| `osdHeader` | 15 | 5 | 1695–1713, 5998–6067, 6093–6118, 6468, 6898 |
| `actionSheetMenuItem` | 11 | 5 | 629, 4223–4234, 4280, 4358–4374, 6449 |
| `sectionTabs` | 10 | 5 | 1789, 3701, 4188, 6039–6044, 6184–6210 |
| `cardImageIcon` | 8 | 5 | 412–416, 2439–2448, 2511, 3437, 5794 |
| `headerTop` | 8 | 5 | 4128, 4161, 6009–6034, 6085–6102, 6129–6133 |
| `sectionTitle` | 7 | 5 | 1726, 1799–1806, 4029, 4757–4765, 5662 |
| `emby-scroller-container` | 6 | 5 | 1726–1731, 1769, 2676, 6477, 6569 |
| `portraitCard` | 6 | 5 | 1076, 1154, 1910–1915, 2150, 2784 |
| `scss` | 5 | 5 | 284, 768, 1028, 3459, 6569 |
| `skinHeader-withBackground` | 5 | 5 | 1634, 3898, 5593, 5998, 6048 |
| `btnPlay` | 16 | 4 | 511–535, 574–629, 3653–3695, 3728–3755 |
| `cardOverlayContainer` | 12 | 4 | 929–961, 1006–1028, 1088, 6898–6916 |
| `itemName` | 11 | 4 | 686, 2257, 5166–5212, 5303–5320 |
| `backdropImage` | 10 | 4 | 2576–2603, 2630–2634, 6385, 6485–6493 |
| `emby-tab-button` | 10 | 4 | 629, 696–705, 3701, 6169–6205 |
| `upNextContainer` | 10 | 4 | 4849–4868, 4894–4920, 6421–6431, 6457 |
| `emby-scroller` | 9 | 4 | 1731, 1769–1775, 6719–6766, 6877–6893 |
| `detailRibbon` | 8 | 4 | 1591–1619, 1825, 1910–1922, 7121 |
| `listItemBodyText` | 7 | 4 | 4244–4263, 4303, 4362, 6933 |
| `visualCardBox` | 7 | 4 | 420, 834–847, 873–878, 1002 |
| `button-submit` | 6 | 4 | 3722, 3809, 5695–5703, 7001–7015 |
| `cardText-secondary` | 6 | 4 | 302, 916, 3442–3446, 6547–6555 |
| `detailPagePrimaryContent` | 6 | 4 | 1606–1624, 2391, 4678, 6633 |
| `skip-button` | 6 | 4 | 629, 3706, 4943–4960, 4987–4993 |
| `squareCard` | 6 | 4 | 857, 2439, 2475–2493, 5671–5675 |
| `skinHeader-blurred` | 5 | 4 | 5593, 6027–6034, 6617, 6898 |
| `appfooter` | 4 | 4 | 2727, 6143, 6508, 6898 |
| `itemsContainer` | 4 | 4 | 740, 1758, 1793, 4684 |
| `raised` | 4 | 4 | 629, 715, 3589, 3624 |
| `detailButton` | 13 | 3 | 574–629, 3634–3695, 3751–3755 |
| `itemSelectionPanel` | 9 | 3 | 886–890, 3382, 3410–3453 |
| `check` | 8 | 3 | 3410, 3643, 4354–4374 |
| `pageTitle` | 8 | 3 | 1670–1713, 6059, 6118 |
| `sectionTitleTextButton` | 8 | 3 | 4740–4748, 4775–4787, 4821–4831 |
| `backgroundContainer` | 7 | 3 | 2567, 2608–2626, 2658 |
| `homePage` | 7 | 3 | 4128, 4161–4188, 6227 |
| `playedIndicator` | 7 | 3 | 768–782, 3526, 6650–6671 |
| `detailSectionContent` | 6 | 3 | 3216, 4479–4489, 4569–4579 |
| `emby-checkbox` | 6 | 3 | 3387, 3424–3428, 3477–3489 |
| `actionSheetContent` | 5 | 3 | 4346–4350, 6421–6431, 6457 |
| `cardText-first` | 5 | 3 | 916, 3416–3442, 5775 |
| `dialog` | 5 | 3 | 3266–3276, 6421–6431, 6457 |
| `guideProgramName` | 5 | 3 | 629, 5344–5355, 5398–5403 |
| `noHomeButtonHeader` | 5 | 3 | 1652, 6059, 6169–6177 |
| `overflowBackdropCard` | 5 | 3 | 955–961, 3420, 5770–5775 |
| `secondary` | 5 | 3 | 302, 4253–4263, 4303 |
| `album` | 4 | 3 | 2186, 2444–2448, 2484 |
| `cardPadder` | 4 | 3 | 416, 1002, 3433–3437 |
| `cardText` | 4 | 3 | 916–926, 3442, 6792 |
| `detailPageContent` | 4 | 3 | 1748, 4410, 4671–4678 |
| `dialog-fullscreen` | 4 | 3 | 3276, 6421–6431, 6457 |
| `emby-scrollbuttons` | 4 | 3 | 1811–1816, 6813, 7273 |
| `folder` | 4 | 3 | 1910–1915, 3543, 3607 |
| `formDialogFooter` | 4 | 3 | 3334, 3816, 6950–6974 |
| `infoWrapper` | 4 | 3 | 2129–2134, 2391, 2419 |
| `listItemImage` | 4 | 3 | 2761–2766, 4217, 6933 |
| `musicParentName` | 4 | 3 | 1986, 2497, 5285–5294 |
| `semiTransparent` | 4 | 3 | 1634, 5593, 6027–6048 |
| `toast` | 4 | 3 | 4841, 6421–6431, 6457 |
| `cardFooter` | 3 | 3 | 3453, 6525, 6560 |
| `defaultCardBackground` | 3 | 3 | 3564, 5790, 5889 |
| `detailPageSecondaryContainer` | 3 | 3 | 1601, 1628, 1748 |
| `formDialogFooterItem` | 3 | 3 | 3334, 3602, 3728 |
| `formDialogHeader` | 3 | 3 | 3816, 6898, 6950 |
| `iconOsd` | 3 | 3 | 5571, 6898, 6950 |
| `live_tv` | 3 | 3 | 1986, 2484, 3850 |
| `myPreferencesMenuPage` | 3 | 3 | 389, 4388, 4692 |
| `page` | 3 | 3 | 998, 2658, 6477 |
| `playerStats` | 3 | 3 | 5571, 6950, 6986 |
| `sectionTitle-cards` | 3 | 3 | 1726, 4757, 4817 |
| `sectionTitleContainer` | 3 | 3 | 1758, 1816, 4603 |
| `x` | 3 | 3 | 2257, 5268, 6569 |
| `itemExternalLinks` | 13 | 2 | 3060–3138, 3216 |
| `checkboxOutline` | 10 | 2 | 3387–3428, 3459–3489 |
| `itemBackdrop` | 9 | 2 | 1952–2007, 2159 |
| `mdl-slider` | 9 | 2 | 2857, 2912–2970 |
| `listItemIcon` | 8 | 2 | 3846–3850, 4358–4388 |
| `sliderContainer` | 8 | 2 | 2861, 2889–2954 |
| `cardOverlayButton-br` | 7 | 2 | 1014, 1043–1081 |
| `detail-clamp-text` | 7 | 2 | 3152–3178, 3204–3208 |
| `divUsers` | 7 | 2 | 5671–5675, 6776–6803 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3424–3428, 3458–3477 |
| `countIndicator` | 6 | 2 | 759–789, 6950–6974 |
| `detailPagePrimaryContainer` | 6 | 2 | 1578–1624, 2391 |
| `detailsGroupItem` | 6 | 2 | 4441, 4509–4546 |
| `headerButton` | 6 | 2 | 549–629, 6111 |
| `headerLeft` | 6 | 2 | 1676–1713, 6314 |
| `selectionCommandsPanel` | 6 | 2 | 3344–3378, 6898 |
| `trackSelections` | 6 | 2 | 4414–4441, 4574–4579 |
| `withBackdrop` | 6 | 2 | 2567, 2608–2626 |
| `detailSection` | 5 | 2 | 4397–4406, 4559–4579 |
| `fullSyncIndicator` | 5 | 2 | 759–782, 6950–6974 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3020, 6689–6706 |
| `mediaInfoItem` | 5 | 2 | 1829–1872, 6569 |
| `overview-expand` | 5 | 2 | 3184–3208, 4479 |
| `scrollX` | 5 | 2 | 1731, 1769–1789 |
| `videoIndicator` | 5 | 2 | 3532–3560, 6950 |
| `withSectionTabs` | 5 | 2 | 2617–2634, 6034 |
| `alphaPickerButton` | 4 | 2 | 629, 4618–4630 |
| `backgroundProgress` | 4 | 2 | 2772–2784, 2814 |
| `emby-tab-button-active` | 4 | 2 | 3788, 6196–6210 |
| `mediaSourceIndicator` | 4 | 2 | 759–782, 6950 |
| `play_arrow` | 4 | 2 | 3569–3585, 3755 |
| `playbackProgress` | 4 | 2 | 2772–2784, 2819 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4244–4249, 5883–5889 |
| `programCell` | 4 | 2 | 5335, 5394–5403 |
| `programGuideSection` | 4 | 2 | 2452–2467, 4579–4594 |
| `section0` | 4 | 2 | 968–998, 6477 |
| `visualLoginForm` | 4 | 2 | 5662–5679, 5720 |
| `cardOverlayButtonIcon` | 3 | 2 | 1014–1026, 1081 |
| `castCollapsible` | 3 | 2 | 825, 3428–3437 |
| `collectionItems` | 3 | 2 | 1758, 4579–4603 |
| `emby-input` | 3 | 2 | 5093–5109, 7015 |
| `emby-scrollbuttons-button` | 3 | 2 | 1820, 7280–7287 |
| `guestCastContent` | 3 | 2 | 825, 3428–3437 |
| `guide-channelHeaderCell` | 3 | 2 | 629, 5369–5385 |
| `guide-date-tab-button` | 3 | 2 | 629, 3788–3796 |
| `headerUserButton` | 3 | 2 | 549–562, 4696 |
| `manualLoginForm` | 3 | 2 | 5662–5679, 5720 |
| `overview` | 3 | 2 | 3204–3208, 4489 |
| `add` | 2 | 2 | 1731, 6569 |
| `alphaPicker-fixed-right` | 2 | 2 | 2658, 4630 |
| `backdropImageFadeIn` | 2 | 2 | 2711, 6990 |
| `book` | 2 | 2 | 1986, 2484 |
| `btnDeleteImage` | 2 | 2 | 3589, 3802 |
| `cardContent` | 2 | 2 | 825, 857 |
| `cardOverlayButton` | 2 | 2 | 1028, 1064 |
| `cardOverlayButton-hover` | 2 | 2 | 911, 1043 |
| `chevron_right` | 2 | 2 | 4787, 4831 |
| `classList` | 2 | 2 | 1731, 6569 |
| `collapseContent` | 2 | 2 | 3339, 3814 |
| `collectionItemsContainer` | 2 | 2 | 1758, 4607 |
| `content-primary` | 2 | 2 | 4671, 4723 |
| `editorsChoiceItemOverview` | 2 | 2 | 7210, 7291 |
| `emby-select` | 2 | 2 | 5093, 7015 |
| `endsAt` | 2 | 2 | 1850, 6569 |
| `fieldDescription` | 2 | 2 | 302, 7015 |
| `formDialogFooter-clear` | 2 | 2 | 3334, 3816 |
| `guide-programNameCaret` | 2 | 2 | 302, 5351 |
| `headroom` | 2 | 2 | 6022, 6059 |
| `indicator` | 2 | 2 | 789, 3521 |
| `mediaInfoOfficialRating` | 2 | 2 | 1850, 6569 |
| `navMenuOption-selected` | 2 | 2 | 4393, 6700 |
| `nowPlayingInfoContainer` | 2 | 2 | 3051, 5820 |
| `org` | 2 | 2 | 3087, 3117 |
| `paperList` | 2 | 2 | 834, 3827 |
| `playlist` | 2 | 2 | 4239, 5798 |
| `programSecondaryTitle` | 2 | 2 | 302, 5403 |
| `queue` | 2 | 2 | 1986, 2484 |
| `readOnlyContent` | 2 | 2 | 3858, 6243 |
| `recordingFields` | 2 | 2 | 4433, 4574 |
| `runtime` | 2 | 2 | 5732, 5760 |
| `sectionTitleContainer-cards` | 2 | 2 | 4752, 4817 |
| `sidebarHeader` | 2 | 2 | 3950, 6706 |
| `tagline` | 2 | 2 | 2558, 4489 |
| `tsx` | 2 | 2 | 4128, 4192 |
| `upNextDialog-title` | 2 | 2 | 4873, 4907 |
| `vertical-list` | 2 | 2 | 1793, 7116 |
| `vertical-wrap` | 2 | 2 | 755, 1758 |
| `videoOsdBottom` | 2 | 2 | 3043, 5989 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3043, 5989 |
| `userPreferencesPage` | 12 | 1 | 7001–7096 |
| `checkboxContainer` | 7 | 1 | 3416–3453 |
| `itemDetailsGroup` | 7 | 1 | 4493–4579 |
| `itemProgressBar` | 6 | 1 | 2761–2795 |
| `trackSelectionFieldContainer` | 6 | 1 | 4452–4475 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7247–7287 |
| `innerCardFooter` | 5 | 1 | 3229–3258 |
| `chapterCardImageContainer` | 4 | 1 | 3229–3258 |
| `endTimeText` | 4 | 1 | 5732–5760 |
| `mainDetailButtons` | 4 | 1 | 3751–3765 |
| `overview-controls` | 4 | 1 | 3204–3216 |
| `startTimeText` | 4 | 1 | 5732–5754 |
| `button-flat` | 3 | 1 | 3024–3034 |
| `cardIndicators` | 3 | 1 | 3506–3516 |
| `cardOverlayFab-primary` | 3 | 1 | 1006–1028 |
| `com` | 3 | 1 | 3093–3111 |
| `content` | 3 | 1 | 4515–4546 |
| `discover-card` | 3 | 1 | 7298–7321 |
| `emby-select-withcolor` | 3 | 1 | 5093–5127 |
| `emby-textarea` | 3 | 1 | 5084–5109 |
| `fab` | 3 | 1 | 3611–3624 |
| `listChildrenCollapsible` | 3 | 1 | 4564–4579 |
| `mdl-slider-background-flex` | 3 | 1 | 2881–2894 |
| `mediaInfoCriticRating` | 3 | 1 | 1891–1900 |
| `nextUpSection` | 3 | 1 | 4559–4579 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5784–5794 |
| `serverInfo` | 3 | 1 | 3831–3840 |
| `transcodingProgress` | 3 | 1 | 2772–2784 |
