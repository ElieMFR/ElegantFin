# Index des composants — ElegantFin Cinema Edition v1.3.19

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.19.css` — 7687 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2127–2160, 2187–2191, 2467–2485, 2521, 6659, 6917–6933, 7011–7033, 7063–7070, 7160, 7565 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2485, 3538, 3649, 3728, 5847, 6673–6683, 6752, 6917, 7054–7070 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2000–2036, 2071–2086, 2122, 2223, 2534, 3983–3994, 4651, 4938, 7393–7431 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1886, 3495, 3654, 3728–3734, 3840, 3998, 4531, 5041, 5075–5085, 5665 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5972–5976, 6056, 6665, 6744–6752, 6792, 6917–6933, 7054 |
| `skinHeader` | 16 | 10 | 284, 4343, 4389–4416, 5855, 6265, 6321–6329, 6355–6380, 6735, 6884, 7502 |
| `nameContainer` | 27 | 9 | 694, 2230–2253, 2294, 2323, 2358–2404, 2441, 2472–2476, 5422–5474, 7393–7431 |
| `emby-button` | 12 | 9 | 620–637, 664–682, 3160, 3269–3276, 3674, 3709, 3862, 4549, 5257 |
| `js` | 9 | 9 | 331, 1652, 1745, 2294, 2898, 3628, 5665, 6836, 7080 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5976, 6683, 6792–6827, 6917, 7206 |
| `parentName` | 23 | 8 | 694, 2235–2253, 2294, 2323, 2358–2404, 5428–5474, 5547, 7393–7431 |
| `detailLogo` | 20 | 8 | 694, 2010–2036, 2071–2086, 2113–2122, 2223–2253, 2323, 2358–2404, 2472 |
| `listItem` | 19 | 8 | 302, 637, 2489, 4451–4477, 4508–4540, 4585, 4626, 7183–7200 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2036, 2196, 2230–2253, 2323, 2358–2404, 2472 |
| `subtitle` | 16 | 8 | 2000–2010, 2122, 2235, 2294, 2413–2423, 2534, 5482–5515, 7393–7431 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2000–2010, 2139, 2223, 2476–2485, 2512, 2821 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6659, 6917, 7206 |
| `nowPlayingBar` | 8 | 8 | 318, 3084, 6108, 6698, 6786, 6870, 6896, 7165 |
| `loginPage` | 16 | 7 | 3807, 5859–5890, 5929, 5957–5976, 6688, 6731, 7043–7070 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4048, 4518–4540, 4632–4637, 6956–6967 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3435–3455, 5341 |
| `verticalSection` | 11 | 6 | 1740, 2723–2728, 4938, 6744, 6836, 7080 |
| `button-link` | 10 | 6 | 637, 664–682, 3034–3043, 3104–3114, 3160, 7356 |
| `person` | 8 | 6 | 2000–2021, 2223, 2476, 2521–2530, 3935, 7388 |
| `mainDrawer` | 7 | 6 | 3048, 4012, 4389, 6688–6698, 6943, 6982 |
| `scss` | 6 | 6 | 284, 776, 1036, 3544, 4054, 6836 |
| `detailImageContainer` | 20 | 5 | 2000–2021, 2127–2191, 2223, 2463–2485, 2512–2530 |
| `osdHeader` | 15 | 5 | 1709–1727, 6260–6329, 6355–6380, 6735, 7165 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4451–4462, 4508, 4585–4626, 6716 |
| `sectionTabs` | 10 | 5 | 1803, 3786, 4416, 6301–6306, 6446–6477 |
| `cardImageIcon` | 8 | 5 | 420–424, 2476–2485, 2548, 3522, 6056 |
| `headerTop` | 8 | 5 | 4343, 4389, 6271–6296, 6347–6364, 6391–6395 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4244, 5011–5019, 5924 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2713, 6744, 6836 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1924–1929, 2187, 2821 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 3983, 5855, 6260, 6310 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3738–3780, 3813–3840 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7165–7183 |
| `itemName` | 11 | 4 | 694, 2294, 5428–5474, 5565–5582 |
| `backdropImage` | 10 | 4 | 2613–2640, 2667–2671, 6652, 6752–6760 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3786, 6431–6472 |
| `upNextContainer` | 10 | 4 | 5103–5122, 5148–5174, 6688–6698, 6724 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 6986–7033, 7144–7160 |
| `backgroundContainer` | 8 | 4 | 2090, 2604, 2645–2663, 2695 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1839, 1924–1936, 7388 |
| `listItemBodyText` | 7 | 4 | 4472–4491, 4531, 4606, 7200 |
| `skip-button` | 7 | 4 | 637, 3791, 5197–5214, 5241–5259 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3807, 3894, 5957–5965, 7268–7282 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3527–3531, 6814–6822 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2428, 4932, 6900 |
| `squareCard` | 6 | 4 | 865, 2476, 2512–2530, 5933–5937 |
| `skinHeader-blurred` | 5 | 4 | 5855, 6289–6296, 6884, 7165 |
| `appfooter` | 4 | 4 | 2764, 6405, 6775, 7165 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4938 |
| `raised` | 4 | 4 | 637, 723, 3674, 3709 |
| `x` | 4 | 4 | 2294, 4054, 5530, 6836 |
| `detailButton` | 13 | 3 | 582–637, 3719–3780, 3836–3840 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3467, 3495–3538 |
| `pageTitle` | 8 | 3 | 1684–1727, 6321, 6380 |
| `sectionTitleTextButton` | 8 | 3 | 4994–5002, 5029–5041, 5075–5085 |
| `homePage` | 7 | 3 | 4343, 4389–4416, 6494 |
| `playedIndicator` | 7 | 3 | 776–790, 3611, 6917–6938 |
| `check` | 6 | 3 | 3495, 3728, 4585–4626 |
| `detailSectionContent` | 6 | 3 | 3301, 4733–4743, 4823–4833 |
| `emby-checkbox` | 6 | 3 | 3472, 3509–3513, 3562–3574 |
| `actionSheetContent` | 5 | 3 | 4577–4581, 6688–6698, 6724 |
| `cardText-first` | 5 | 3 | 924, 3501–3527, 6037 |
| `dialog` | 5 | 3 | 3351–3361, 6688–6698, 6724 |
| `guideProgramName` | 5 | 3 | 637, 5606–5617, 5660–5665 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6321, 6431–6439 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3505, 6032–6037 |
| `secondary` | 5 | 3 | 302, 4481–4491, 4531 |
| `album` | 4 | 3 | 2223, 2481–2485, 2521 |
| `cardPadder` | 4 | 3 | 424, 1010, 3518–3522 |
| `cardText` | 4 | 3 | 924–934, 3527, 7059 |
| `detailPageContent` | 4 | 3 | 1762, 4664, 4925–4932 |
| `dialog-fullscreen` | 4 | 3 | 3361, 6688–6698, 6724 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7080, 7540 |
| `folder` | 4 | 3 | 1924–1929, 3628, 3692 |
| `formDialogFooter` | 4 | 3 | 3419, 3901, 7217–7241 |
| `infoWrapper` | 4 | 3 | 2166–2171, 2428, 2456 |
| `listItemImage` | 4 | 3 | 2798–2803, 4445, 7200 |
| `musicParentName` | 4 | 3 | 2000, 2534, 5547–5556 |
| `semiTransparent` | 4 | 3 | 1648, 5855, 6289–6310 |
| `toast` | 4 | 3 | 5095, 6688–6698, 6724 |
| `cardFooter` | 3 | 3 | 3538, 6792, 6827 |
| `defaultCardBackground` | 3 | 3 | 3649, 6052, 6151 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `formDialogFooterItem` | 3 | 3 | 3419, 3687, 3813 |
| `formDialogHeader` | 3 | 3 | 3901, 7165, 7217 |
| `iconOsd` | 3 | 3 | 5833, 7165, 7217 |
| `live_tv` | 3 | 3 | 2000, 2521, 3935 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4642, 4946 |
| `page` | 3 | 3 | 1006, 2695, 6744 |
| `playerStats` | 3 | 3 | 5833, 7217, 7253 |
| `sectionTitle-cards` | 3 | 3 | 1740, 5011, 5071 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4857 |
| `tsx` | 3 | 3 | 1084, 4343, 4420 |
| `itemExternalLinks` | 13 | 2 | 3097–3175, 3301 |
| `checkboxOutline` | 10 | 2 | 3472–3513, 3544–3574 |
| `itemBackdrop` | 9 | 2 | 1966–2021, 2196 |
| `mdl-slider` | 9 | 2 | 2894, 2949–3007 |
| `listItemIcon` | 8 | 2 | 3931–3935, 4585–4642 |
| `sliderContainer` | 8 | 2 | 2898, 2926–2991 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3237–3263, 3289–3293 |
| `divUsers` | 7 | 2 | 5933–5937, 7043–7070 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3509–3513, 3543–3562 |
| `countIndicator` | 6 | 2 | 767–797, 7217–7241 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2428 |
| `detailsGroupItem` | 6 | 2 | 4695, 4763–4800 |
| `headerButton` | 6 | 2 | 557–637, 6373 |
| `headerLeft` | 6 | 2 | 1690–1727, 6581 |
| `selectionCommandsPanel` | 6 | 2 | 3429–3463, 7165 |
| `trackSelections` | 6 | 2 | 4668–4695, 4828–4833 |
| `withBackdrop` | 6 | 2 | 2604, 2645–2663 |
| `detailSection` | 5 | 2 | 4651–4660, 4813–4833 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7217–7241 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3057, 6956–6973 |
| `mediaInfoItem` | 5 | 2 | 1843–1886, 6836 |
| `overview-expand` | 5 | 2 | 3269–3293, 4733 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3617–3645, 7217 |
| `withSectionTabs` | 5 | 2 | 2654–2671, 6296 |
| `alphaPickerButton` | 4 | 2 | 637, 4872–4884 |
| `backgroundProgress` | 4 | 2 | 2809–2821, 2851 |
| `emby-tab-button-active` | 4 | 2 | 3873, 6463–6477 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7217 |
| `play_arrow` | 4 | 2 | 3654–3670, 3840 |
| `playbackProgress` | 4 | 2 | 2809–2821, 2856 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4472–4477, 6145–6151 |
| `programCell` | 4 | 2 | 5597, 5656–5665 |
| `programGuideSection` | 4 | 2 | 2489–2504, 4833–4848 |
| `section0` | 4 | 2 | 976–1006, 6744 |
| `visualLoginForm` | 4 | 2 | 5924–5941, 5982 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3513–3522 |
| `collectionItems` | 3 | 2 | 1772, 4833–4857 |
| `emby-input` | 3 | 2 | 5355–5371, 7282 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7547–7554 |
| `guestCastContent` | 3 | 2 | 833, 3513–3522 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5631–5647 |
| `guide-date-tab-button` | 3 | 2 | 637, 3873–3881 |
| `headerUserButton` | 3 | 2 | 557–570, 4950 |
| `manualLoginForm` | 3 | 2 | 5924–5941, 5982 |
| `overview` | 3 | 2 | 3289–3293, 4743 |
| `add` | 2 | 2 | 1745, 6836 |
| `alphaPicker-fixed-right` | 2 | 2 | 2695, 4884 |
| `backdropImageFadeIn` | 2 | 2 | 2748, 7257 |
| `book` | 2 | 2 | 2000, 2521 |
| `btnDeleteImage` | 2 | 2 | 3674, 3887 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 5041, 5085 |
| `classList` | 2 | 2 | 1745, 6836 |
| `collapseContent` | 2 | 2 | 3424, 3899 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4861 |
| `content-primary` | 2 | 2 | 4925, 4977 |
| `editorsChoiceItemOverview` | 2 | 2 | 7477, 7558 |
| `emby-select` | 2 | 2 | 5355, 7282 |
| `endsAt` | 2 | 2 | 1864, 6836 |
| `fieldDescription` | 2 | 2 | 302, 7282 |
| `formDialogFooter-clear` | 2 | 2 | 3419, 3901 |
| `guide-programNameCaret` | 2 | 2 | 302, 5613 |
| `headroom` | 2 | 2 | 6284, 6321 |
| `indicator` | 2 | 2 | 797, 3606 |
| `mediaInfoOfficialRating` | 2 | 2 | 1864, 6836 |
| `navMenuOption-selected` | 2 | 2 | 4647, 6967 |
| `nowPlayingInfoContainer` | 2 | 2 | 3088, 6082 |
| `org` | 2 | 2 | 3124, 3154 |
| `paperList` | 2 | 2 | 842, 3912 |
| `playlist` | 2 | 2 | 4467, 6060 |
| `programSecondaryTitle` | 2 | 2 | 302, 5665 |
| `queue` | 2 | 2 | 2000, 2521 |
| `reactRoot` | 2 | 2 | 4343, 6587 |
| `readOnlyContent` | 2 | 2 | 3943, 6510 |
| `recordingFields` | 2 | 2 | 4687, 4828 |
| `runtime` | 2 | 2 | 5994, 6022 |
| `sectionTitleContainer-cards` | 2 | 2 | 5006, 5071 |
| `sidebarHeader` | 2 | 2 | 4035, 6973 |
| `tagline` | 2 | 2 | 2595, 4743 |
| `upNextDialog-title` | 2 | 2 | 5127, 5161 |
| `vertical-list` | 2 | 2 | 1807, 7383 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3080, 6251 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3080, 6251 |
| `userPreferencesPage` | 12 | 1 | 7268–7363 |
| `checkboxContainer` | 7 | 1 | 3501–3538 |
| `itemDetailsGroup` | 7 | 1 | 4747–4833 |
| `itemProgressBar` | 6 | 1 | 2798–2832 |
| `streaming-lookup-container` | 6 | 1 | 3182–3226 |
| `trackSelectionFieldContainer` | 6 | 1 | 4706–4729 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7514–7554 |
| `innerCardFooter` | 5 | 1 | 3314–3343 |
| `chapterCardImageContainer` | 4 | 1 | 3314–3343 |
| `endTimeText` | 4 | 1 | 5994–6022 |
| `mainDetailButtons` | 4 | 1 | 3836–3850 |
| `overview-controls` | 4 | 1 | 3289–3301 |
| `startTimeText` | 4 | 1 | 5994–6016 |
| `button-flat` | 3 | 1 | 3061–3071 |
| `cardIndicators` | 3 | 1 | 3591–3601 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3130–3148 |
| `content` | 3 | 1 | 4769–4800 |
| `discover-card` | 3 | 1 | 7565–7588 |
| `emby-select-withcolor` | 3 | 1 | 5355–5389 |
| `emby-textarea` | 3 | 1 | 5346–5371 |
| `fab` | 3 | 1 | 3696–3709 |
| `listChildrenCollapsible` | 3 | 1 | 4818–4833 |
| `mdl-slider-background-flex` | 3 | 1 | 2918–2931 |
| `mediaInfoCriticRating` | 3 | 1 | 1905–1914 |
| `nextUpSection` | 3 | 1 | 4813–4833 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6046–6056 |
| `serverInfo` | 3 | 1 | 3916–3925 |
| `transcodingProgress` | 3 | 1 | 2809–2821 |
