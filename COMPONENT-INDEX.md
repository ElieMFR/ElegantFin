# Index des composants — ElegantFin Cinema Edition v1.3.15

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.15.css` — 7483 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1511–1531, 2121–2154, 2181–2185, 2461–2479, 2515, 6455, 6713–6729, 6807–6829, 6859–6866, 6956, 7361 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2479, 3484, 3595, 3674, 5648, 6469–6479, 6548, 6713, 6850–6866 |
| `itemDetailPage` | 21 | 13 | 1574, 1660, 1739, 1766, 1994–2030, 2065–2080, 2116, 2217, 2528, 3929–3940, 4464, 4751, 7189–7227 |
| `material-icons` | 17 | 13 | 364–383, 1730, 1828, 1880, 3441, 3600, 3674–3680, 3786, 3944, 4347, 4854, 4888–4898, 5466 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5773–5777, 5857, 6461, 6540–6548, 6588, 6713–6729, 6850 |
| `skinHeader` | 16 | 10 | 284, 4159, 4205–4232, 5656, 6066, 6122–6130, 6156–6181, 6531, 6680, 7298 |
| `nameContainer` | 27 | 9 | 694, 2224–2247, 2288, 2317, 2352–2398, 2435, 2466–2470, 5223–5275, 7189–7227 |
| `js` | 9 | 9 | 331, 1646, 1739, 2288, 2892, 3574, 5466, 6632, 6876 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5777, 6479, 6588–6623, 6713, 7002 |
| `parentName` | 23 | 8 | 694, 2229–2247, 2288, 2317, 2352–2398, 5229–5275, 5348, 7189–7227 |
| `detailLogo` | 20 | 8 | 694, 2004–2030, 2065–2080, 2107–2116, 2217–2247, 2317, 2352–2398, 2466 |
| `listItem` | 19 | 8 | 302, 637, 2483, 4267–4293, 4324–4356, 4398, 4439, 6979–6996 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1542–1552, 2030, 2190, 2224–2247, 2317, 2352–2398, 2466 |
| `subtitle` | 16 | 8 | 1994–2004, 2116, 2229, 2288, 2407–2417, 2528, 5283–5316, 7189–7227 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 1994–2004, 2133, 2217, 2470–2479, 2506, 2815 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6455, 6713, 7002 |
| `emby-button` | 11 | 8 | 620–637, 664–682, 3154, 3215–3222, 3620, 3655, 3808, 4365 |
| `nowPlayingBar` | 8 | 8 | 318, 3078, 5909, 6494, 6582, 6666, 6692, 6961 |
| `loginPage` | 16 | 7 | 3753, 5660–5691, 5730, 5758–5777, 6484, 6527, 6839–6866 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 3994, 4334–4356, 4445–4450, 6752–6763 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1660, 1730, 1828, 3381–3401, 5142 |
| `verticalSection` | 11 | 6 | 1734, 2717–2722, 4751, 6540, 6632, 6876 |
| `button-link` | 10 | 6 | 637, 664–682, 3028–3037, 3098–3108, 3154, 7152 |
| `person` | 8 | 6 | 1994–2015, 2217, 2470, 2515–2524, 3881, 7184 |
| `mainDrawer` | 7 | 6 | 3042, 3958, 4205, 6484–6494, 6739, 6778 |
| `detailImageContainer` | 20 | 5 | 1994–2015, 2121–2185, 2217, 2457–2479, 2506–2524 |
| `osdHeader` | 15 | 5 | 1703–1721, 6061–6130, 6156–6181, 6531, 6961 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4267–4278, 4324, 4398–4439, 6512 |
| `sectionTabs` | 10 | 5 | 1797, 3732, 4232, 6102–6107, 6247–6273 |
| `cardImageIcon` | 8 | 5 | 420–424, 2470–2479, 2542, 3468, 5857 |
| `headerTop` | 8 | 5 | 4159, 4205, 6072–6097, 6148–6165, 6192–6196 |
| `sectionTitle` | 7 | 5 | 1734, 1807–1814, 4060, 4824–4832, 5725 |
| `emby-scroller-container` | 6 | 5 | 1734–1739, 1777, 2707, 6540, 6632 |
| `portraitCard` | 6 | 5 | 1084, 1162, 1918–1923, 2181, 2815 |
| `scss` | 5 | 5 | 284, 776, 1036, 3490, 6632 |
| `skinHeader-withBackground` | 5 | 5 | 1642, 3929, 5656, 6061, 6111 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3684–3726, 3759–3786 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1096, 6961–6979 |
| `itemName` | 11 | 4 | 694, 2288, 5229–5275, 5366–5383 |
| `backdropImage` | 10 | 4 | 2607–2634, 2661–2665, 6448, 6548–6556 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3732, 6232–6268 |
| `upNextContainer` | 10 | 4 | 4916–4935, 4961–4987, 6484–6494, 6520 |
| `emby-scroller` | 9 | 4 | 1739, 1777–1783, 6782–6829, 6940–6956 |
| `backgroundContainer` | 8 | 4 | 2084, 2598, 2639–2657, 2689 |
| `detailRibbon` | 8 | 4 | 1599–1627, 1833, 1918–1930, 7184 |
| `listItemBodyText` | 7 | 4 | 4288–4307, 4347, 4419, 6996 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3753, 3840, 5758–5766, 7064–7078 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3473–3477, 6610–6618 |
| `detailPagePrimaryContent` | 6 | 4 | 1614–1632, 2422, 4745, 6696 |
| `skip-button` | 6 | 4 | 637, 3737, 5010–5027, 5054–5060 |
| `squareCard` | 6 | 4 | 865, 2470, 2506–2524, 5734–5738 |
| `skinHeader-blurred` | 5 | 4 | 5656, 6090–6097, 6680, 6961 |
| `appfooter` | 4 | 4 | 2758, 6206, 6571, 6961 |
| `itemsContainer` | 4 | 4 | 748, 1766, 1801, 4751 |
| `raised` | 4 | 4 | 637, 723, 3620, 3655 |
| `detailButton` | 13 | 3 | 582–637, 3665–3726, 3782–3786 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3413, 3441–3484 |
| `pageTitle` | 8 | 3 | 1678–1721, 6122, 6181 |
| `sectionTitleTextButton` | 8 | 3 | 4807–4815, 4842–4854, 4888–4898 |
| `homePage` | 7 | 3 | 4159, 4205–4232, 6290 |
| `playedIndicator` | 7 | 3 | 776–790, 3557, 6713–6734 |
| `check` | 6 | 3 | 3441, 3674, 4398–4439 |
| `detailSectionContent` | 6 | 3 | 3247, 4546–4556, 4636–4646 |
| `emby-checkbox` | 6 | 3 | 3418, 3455–3459, 3508–3520 |
| `actionSheetContent` | 5 | 3 | 4390–4394, 6484–6494, 6520 |
| `cardText-first` | 5 | 3 | 924, 3447–3473, 5838 |
| `dialog` | 5 | 3 | 3297–3307, 6484–6494, 6520 |
| `guideProgramName` | 5 | 3 | 637, 5407–5418, 5461–5466 |
| `noHomeButtonHeader` | 5 | 3 | 1660, 6122, 6232–6240 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3451, 5833–5838 |
| `secondary` | 5 | 3 | 302, 4297–4307, 4347 |
| `album` | 4 | 3 | 2217, 2475–2479, 2515 |
| `cardPadder` | 4 | 3 | 424, 1010, 3464–3468 |
| `cardText` | 4 | 3 | 924–934, 3473, 6855 |
| `detailPageContent` | 4 | 3 | 1756, 4477, 4738–4745 |
| `dialog-fullscreen` | 4 | 3 | 3307, 6484–6494, 6520 |
| `emby-scrollbuttons` | 4 | 3 | 1819–1824, 6876, 7336 |
| `folder` | 4 | 3 | 1918–1923, 3574, 3638 |
| `formDialogFooter` | 4 | 3 | 3365, 3847, 7013–7037 |
| `infoWrapper` | 4 | 3 | 2160–2165, 2422, 2450 |
| `listItemImage` | 4 | 3 | 2792–2797, 4261, 6996 |
| `musicParentName` | 4 | 3 | 1994, 2528, 5348–5357 |
| `semiTransparent` | 4 | 3 | 1642, 5656, 6090–6111 |
| `toast` | 4 | 3 | 4908, 6484–6494, 6520 |
| `cardFooter` | 3 | 3 | 3484, 6588, 6623 |
| `defaultCardBackground` | 3 | 3 | 3595, 5853, 5952 |
| `detailPageSecondaryContainer` | 3 | 3 | 1609, 1636, 1756 |
| `formDialogFooterItem` | 3 | 3 | 3365, 3633, 3759 |
| `formDialogHeader` | 3 | 3 | 3847, 6961, 7013 |
| `iconOsd` | 3 | 3 | 5634, 6961, 7013 |
| `live_tv` | 3 | 3 | 1994, 2515, 3881 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4455, 4759 |
| `page` | 3 | 3 | 1006, 2689, 6540 |
| `playerStats` | 3 | 3 | 5634, 7013, 7049 |
| `sectionTitle-cards` | 3 | 3 | 1734, 4824, 4884 |
| `sectionTitleContainer` | 3 | 3 | 1766, 1824, 4670 |
| `x` | 3 | 3 | 2288, 5331, 6632 |
| `itemExternalLinks` | 13 | 2 | 3091–3169, 3247 |
| `checkboxOutline` | 10 | 2 | 3418–3459, 3490–3520 |
| `itemBackdrop` | 9 | 2 | 1960–2015, 2190 |
| `mdl-slider` | 9 | 2 | 2888, 2943–3001 |
| `listItemIcon` | 8 | 2 | 3877–3881, 4398–4455 |
| `sliderContainer` | 8 | 2 | 2892, 2920–2985 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1089 |
| `detail-clamp-text` | 7 | 2 | 3183–3209, 3235–3239 |
| `divUsers` | 7 | 2 | 5734–5738, 6839–6866 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3455–3459, 3489–3508 |
| `countIndicator` | 6 | 2 | 767–797, 7013–7037 |
| `detailPagePrimaryContainer` | 6 | 2 | 1586–1632, 2422 |
| `detailsGroupItem` | 6 | 2 | 4508, 4576–4613 |
| `headerButton` | 6 | 2 | 557–637, 6174 |
| `headerLeft` | 6 | 2 | 1684–1721, 6377 |
| `selectionCommandsPanel` | 6 | 2 | 3375–3409, 6961 |
| `trackSelections` | 6 | 2 | 4481–4508, 4641–4646 |
| `withBackdrop` | 6 | 2 | 2598, 2639–2657 |
| `detailSection` | 5 | 2 | 4464–4473, 4626–4646 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7013–7037 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3051, 6752–6769 |
| `mediaInfoItem` | 5 | 2 | 1837–1880, 6632 |
| `overview-expand` | 5 | 2 | 3215–3239, 4546 |
| `scrollX` | 5 | 2 | 1739, 1777–1797 |
| `videoIndicator` | 5 | 2 | 3563–3591, 7013 |
| `withSectionTabs` | 5 | 2 | 2648–2665, 6097 |
| `alphaPickerButton` | 4 | 2 | 637, 4685–4697 |
| `backgroundProgress` | 4 | 2 | 2803–2815, 2845 |
| `emby-tab-button-active` | 4 | 2 | 3819, 6259–6273 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7013 |
| `play_arrow` | 4 | 2 | 3600–3616, 3786 |
| `playbackProgress` | 4 | 2 | 2803–2815, 2850 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4288–4293, 5946–5952 |
| `programCell` | 4 | 2 | 5398, 5457–5466 |
| `programGuideSection` | 4 | 2 | 2483–2498, 4646–4661 |
| `section0` | 4 | 2 | 976–1006, 6540 |
| `visualLoginForm` | 4 | 2 | 5725–5742, 5783 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1089 |
| `castCollapsible` | 3 | 2 | 833, 3459–3468 |
| `collectionItems` | 3 | 2 | 1766, 4646–4670 |
| `emby-input` | 3 | 2 | 5156–5172, 7078 |
| `emby-scrollbuttons-button` | 3 | 2 | 1828, 7343–7350 |
| `guestCastContent` | 3 | 2 | 833, 3459–3468 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5432–5448 |
| `guide-date-tab-button` | 3 | 2 | 637, 3819–3827 |
| `headerUserButton` | 3 | 2 | 557–570, 4763 |
| `manualLoginForm` | 3 | 2 | 5725–5742, 5783 |
| `overview` | 3 | 2 | 3235–3239, 4556 |
| `add` | 2 | 2 | 1739, 6632 |
| `alphaPicker-fixed-right` | 2 | 2 | 2689, 4697 |
| `backdropImageFadeIn` | 2 | 2 | 2742, 7053 |
| `book` | 2 | 2 | 1994, 2515 |
| `btnDeleteImage` | 2 | 2 | 3620, 3833 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 4854, 4898 |
| `classList` | 2 | 2 | 1739, 6632 |
| `collapseContent` | 2 | 2 | 3370, 3845 |
| `collectionItemsContainer` | 2 | 2 | 1766, 4674 |
| `content-primary` | 2 | 2 | 4738, 4790 |
| `editorsChoiceItemOverview` | 2 | 2 | 7273, 7354 |
| `emby-select` | 2 | 2 | 5156, 7078 |
| `endsAt` | 2 | 2 | 1858, 6632 |
| `fieldDescription` | 2 | 2 | 302, 7078 |
| `formDialogFooter-clear` | 2 | 2 | 3365, 3847 |
| `guide-programNameCaret` | 2 | 2 | 302, 5414 |
| `headroom` | 2 | 2 | 6085, 6122 |
| `indicator` | 2 | 2 | 797, 3552 |
| `mediaInfoOfficialRating` | 2 | 2 | 1858, 6632 |
| `navMenuOption-selected` | 2 | 2 | 4460, 6763 |
| `nowPlayingInfoContainer` | 2 | 2 | 3082, 5883 |
| `org` | 2 | 2 | 3118, 3148 |
| `paperList` | 2 | 2 | 842, 3858 |
| `playlist` | 2 | 2 | 4283, 5861 |
| `programSecondaryTitle` | 2 | 2 | 302, 5466 |
| `queue` | 2 | 2 | 1994, 2515 |
| `reactRoot` | 2 | 2 | 4159, 6383 |
| `readOnlyContent` | 2 | 2 | 3889, 6306 |
| `recordingFields` | 2 | 2 | 4500, 4641 |
| `runtime` | 2 | 2 | 5795, 5823 |
| `sectionTitleContainer-cards` | 2 | 2 | 4819, 4884 |
| `sidebarHeader` | 2 | 2 | 3981, 6769 |
| `tagline` | 2 | 2 | 2589, 4556 |
| `tsx` | 2 | 2 | 4159, 4236 |
| `upNextDialog-title` | 2 | 2 | 4940, 4974 |
| `vertical-list` | 2 | 2 | 1801, 7179 |
| `vertical-wrap` | 2 | 2 | 763, 1766 |
| `videoOsdBottom` | 2 | 2 | 3074, 6052 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3074, 6052 |
| `userPreferencesPage` | 12 | 1 | 7064–7159 |
| `checkboxContainer` | 7 | 1 | 3447–3484 |
| `itemDetailsGroup` | 7 | 1 | 4560–4646 |
| `itemProgressBar` | 6 | 1 | 2792–2826 |
| `trackSelectionFieldContainer` | 6 | 1 | 4519–4542 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7310–7350 |
| `innerCardFooter` | 5 | 1 | 3260–3289 |
| `chapterCardImageContainer` | 4 | 1 | 3260–3289 |
| `endTimeText` | 4 | 1 | 5795–5823 |
| `mainDetailButtons` | 4 | 1 | 3782–3796 |
| `overview-controls` | 4 | 1 | 3235–3247 |
| `startTimeText` | 4 | 1 | 5795–5817 |
| `button-flat` | 3 | 1 | 3055–3065 |
| `cardIndicators` | 3 | 1 | 3537–3547 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3124–3142 |
| `content` | 3 | 1 | 4582–4613 |
| `discover-card` | 3 | 1 | 7361–7384 |
| `emby-select-withcolor` | 3 | 1 | 5156–5190 |
| `emby-textarea` | 3 | 1 | 5147–5172 |
| `fab` | 3 | 1 | 3642–3655 |
| `listChildrenCollapsible` | 3 | 1 | 4631–4646 |
| `mdl-slider-background-flex` | 3 | 1 | 2912–2925 |
| `mediaInfoCriticRating` | 3 | 1 | 1899–1908 |
| `nextUpSection` | 3 | 1 | 4626–4646 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5847–5857 |
| `serverInfo` | 3 | 1 | 3862–3871 |
| `transcodingProgress` | 3 | 1 | 2803–2815 |
