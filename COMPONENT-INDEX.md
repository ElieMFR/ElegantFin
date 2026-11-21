# Index des composants — ElegantFin Cinema Edition v1.5.9

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.9.css` — 8092 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 451–481, 512–547, 785, 898, 1559–1579, 2188–2221, 2248–2252, 2529–2547, 2583, 6994, 7030–7040, 7180, 7280–7299, 7377–7399, 7429–7436, 7606 |
| `cardScalable` | 29 | 14 | 451, 481, 535–547, 848–888, 914–958, 2547, 3641, 3753, 3830, 6060, 7008–7040, 7110, 7280, 7420–7436 |
| `cardImageContainer` | 21 | 13 | 462, 530, 866, 894–923, 958, 1016–1040, 6214–6218, 6298, 7000, 7110, 7150, 7280–7299, 7420 |
| `material-icons` | 17 | 13 | 393–412, 1779, 1877, 1930, 3598, 3758, 3830–3836, 3961, 4122, 4684, 5213, 5247–5255, 5881 |
| `itemDetailPage` | 20 | 12 | 1622, 1703, 1788, 1815, 2044–2084, 2119–2134, 2170–2174, 2284, 2596, 4811, 5106, 7859–7897 |
| `skinHeader` | 20 | 12 | 296, 1703, 4102–4118, 4496, 4542–4569, 6068–6072, 6507, 6563–6571, 6641–6666, 7094, 7247, 7930 |
| `js` | 13 | 12 | 330, 360, 1689–1703, 1788, 2355, 2958, 3402, 3732, 5881, 6872, 7199, 7446 |
| `emby-button` | 14 | 11 | 657–674, 701–719, 3236, 3370–3377, 3778, 3811, 3923, 3983, 4702, 5389, 5442 |
| `nameContainer` | 27 | 9 | 731, 2291–2314, 2355, 2384, 2419–2466, 2503, 2534–2538, 5637–5690, 7859–7897 |
| `parentName` | 23 | 8 | 731, 2296–2314, 2355, 2384, 2419–2466, 5643–5690, 5763, 7859–7897 |
| `detailLogo` | 20 | 8 | 731, 2073–2084, 2119–2134, 2161–2174, 2284–2314, 2384, 2419–2466, 2534 |
| `detailPageWrapperContainer` | 17 | 8 | 731, 1590–1600, 2084, 2257, 2291–2314, 2384, 2419–2466, 2534 |
| `subtitle` | 17 | 8 | 2044–2054, 2170–2174, 2296, 2355, 2475–2485, 2596, 5698–5731, 7859–7897 |
| `cardBox` | 13 | 8 | 451–481, 512–536, 785, 936–940, 1045, 6994, 7280, 7671 |
| `backdropCard` | 12 | 8 | 1003–1009, 1126, 2044–2054, 2200, 2284, 2538–2547, 2574, 2891 |
| `nowPlayingBar` | 8 | 8 | 330, 3160, 6350, 7057, 7144, 7233, 7259, 7611 |
| `card-hoverable` | 22 | 7 | 547, 914–1009, 6218, 7018, 7150–7189, 7280, 7671 |
| `loginPage` | 19 | 7 | 3917–3923, 6072–6106, 6144–6163, 6199–6218, 7047, 7090, 7409–7436 |
| `listItem` | 18 | 7 | 314, 674, 2551, 4604–4630, 4661–4693, 4738, 7648–7665 |
| `paper-icon-button-light` | 12 | 7 | 619–674, 1703, 1779, 1877, 3538–3558, 5389, 5526 |
| `navMenuOption` | 12 | 6 | 674, 770–780, 4171, 4671–4693, 4792–4797, 7322–7333 |
| `emby-tab-button` | 11 | 6 | 674, 741–750, 3892, 6717–6728, 6756–6773, 7942 |
| `verticalSection` | 11 | 6 | 1783, 2783–2788, 5106, 7103, 7199, 7446 |
| `button-link` | 10 | 6 | 674, 701–719, 3111–3120, 3180–3190, 3236, 7822 |
| `headerTop` | 9 | 6 | 2174, 4496, 4542, 6513–6538, 6633–6650, 6677–6681 |
| `person` | 8 | 6 | 2044–2069, 2284, 2538, 2583–2592, 4054, 7854 |
| `mainDrawer` | 7 | 6 | 3125, 4136, 4542, 7047–7057, 7309, 7348 |
| `scss` | 6 | 6 | 296, 813, 1071, 3647, 4177, 7199 |
| `detailImageContainer` | 20 | 5 | 2044–2069, 2188–2252, 2284, 2525–2547, 2574–2592 |
| `btnPlay` | 19 | 5 | 556–580, 619–674, 3840–3891, 3933–3961, 5389 |
| `osdHeader` | 15 | 5 | 1752–1770, 6502–6571, 6641–6666, 7094, 7611 |
| `cardOverlayContainer` | 12 | 5 | 977–1009, 1049–1071, 1144, 7611, 7648 |
| `sectionTabs` | 11 | 5 | 1846, 3892, 4569, 6543–6548, 6734–6778 |
| `cardImageIcon` | 8 | 5 | 443–447, 2538–2547, 2610, 3625, 6298 |
| `sectionTitle` | 7 | 5 | 1783, 1856–1863, 4389, 5183–5191, 6139 |
| `semiTransparent` | 7 | 5 | 1685, 4102–4118, 6068, 6531–6552, 6588 |
| `emby-scroller-container` | 6 | 5 | 1783–1788, 1826, 2771, 7103, 7199 |
| `portraitCard` | 6 | 5 | 1126, 1210, 1968–1973, 2248, 2891 |
| `appfooter` | 5 | 5 | 330, 2834, 6691, 7133, 7611 |
| `skinHeader-withBackground` | 5 | 5 | 1685, 4102, 6068, 6502, 6552 |
| `detailButton` | 15 | 4 | 619–674, 3821–3891, 3957–3961, 5389 |
| `itemName` | 11 | 4 | 731, 2355, 5643–5690, 5781–5798 |
| `backdropImage` | 10 | 4 | 2670–2698, 2725–2729, 6987, 7110–7118 |
| `upNextContainer` | 10 | 4 | 5272–5290, 5316–5342, 7047–7057, 7083 |
| `emby-scroller` | 9 | 4 | 1788, 1826–1832, 7352–7399, 7590–7606 |
| `sectionTitleTextButton` | 9 | 4 | 473, 5166–5174, 5201–5213, 5247–5255 |
| `skip-button` | 9 | 4 | 674, 3901, 5365–5399, 5426–5444 |
| `backgroundContainer` | 8 | 4 | 2138, 2662, 2703–2721, 2753 |
| `detailRibbon` | 8 | 4 | 1647–1671, 1883, 1968–1980, 7854 |
| `button-submit` | 7 | 4 | 3917–3923, 4013, 6199–6207, 7733–7748 |
| `visualCardBox` | 7 | 4 | 451, 875–888, 914–919, 1045 |
| `actionSheetMenuItem` | 6 | 4 | 674, 4604–4615, 4661, 7075 |
| `cardText-secondary` | 6 | 4 | 314, 963, 3630–3634, 7172–7180 |
| `skinHeader-blurred` | 6 | 4 | 6068, 6531–6538, 7247, 7611–7630 |
| `squareCard` | 6 | 4 | 898, 2538, 2574–2592, 6168–6172 |
| `itemsContainer` | 4 | 4 | 785, 1815, 1850, 5106 |
| `raised` | 4 | 4 | 674, 760, 3778, 3811 |
| `tsx` | 4 | 4 | 1126, 1703, 4496, 4573 |
| `x` | 4 | 4 | 2355, 4177, 5746, 7199 |
| `itemSelectionPanel` | 9 | 3 | 927–931, 3570, 3598–3641 |
| `pageTitle` | 8 | 3 | 1727–1770, 6563, 6666 |
| `sliderContainer` | 8 | 3 | 2958, 2986–3024, 3061–3068 |
| `headerButton` | 7 | 3 | 594–674, 5389, 6659 |
| `homePage` | 7 | 3 | 4496, 4542–4569, 6795 |
| `playedIndicator` | 7 | 3 | 813–827, 3714, 7280–7304 |
| `detailSectionContent` | 6 | 3 | 3402, 4893–4903, 4986–4996 |
| `emby-checkbox` | 6 | 3 | 3575, 3612–3616, 3665–3677 |
| `listItemBodyText` | 6 | 3 | 4625–4644, 4684, 7665 |
| `actionSheetContent` | 5 | 3 | 4730–4734, 7047–7057, 7083 |
| `cardText-first` | 5 | 3 | 963, 3604–3630, 6279 |
| `detailPagePrimaryContent` | 5 | 3 | 1660–1676, 2490, 7263 |
| `dialog` | 5 | 3 | 3454–3464, 7047–7057, 7083 |
| `emby-input` | 5 | 3 | 5540–5550, 5578–5596, 7748 |
| `guideProgramName` | 5 | 3 | 674, 5822–5833, 5876–5881 |
| `noHomeButtonHeader` | 5 | 3 | 1703, 6563, 6717–6728 |
| `overflowBackdropCard` | 5 | 3 | 1003–1009, 3608, 6274–6279 |
| `secondary` | 5 | 3 | 314, 4634–4644, 4684 |
| `album` | 4 | 3 | 2284, 2543–2547, 2583 |
| `cardPadder` | 4 | 3 | 447, 1045, 3621–3625 |
| `cardText` | 4 | 3 | 963–973, 3630, 7425 |
| `dialog-fullscreen` | 4 | 3 | 3464, 7047–7057, 7083 |
| `emby-scrollbuttons` | 4 | 3 | 1868–1873, 7446, 7976 |
| `folder` | 4 | 3 | 1968–1973, 3732, 3794 |
| `formDialogFooter` | 4 | 3 | 3522, 4020, 7682–7706 |
| `infoWrapper` | 4 | 3 | 2227–2232, 2490, 2518 |
| `listItemIcon` | 4 | 3 | 4050–4054, 4738, 4802 |
| `listItemImage` | 4 | 3 | 2868–2873, 4598, 7665 |
| `musicParentName` | 4 | 3 | 2044, 2596, 5763–5772 |
| `programGuideSection` | 4 | 3 | 2551–2566, 4996, 5023 |
| `toast` | 4 | 3 | 5265, 7047–7057, 7083 |
| `cardFooter` | 3 | 3 | 3641, 7150, 7189 |
| `check` | 3 | 3 | 3598, 3830, 4738 |
| `collectionItems` | 3 | 3 | 1815, 4996, 5032 |
| `defaultCardBackground` | 3 | 3 | 3753, 6294, 6393 |
| `formDialogFooterItem` | 3 | 3 | 3522, 3789, 3933 |
| `formDialogHeader` | 3 | 3 | 4020, 7611, 7682 |
| `iconOsd` | 3 | 3 | 6046, 7611, 7682 |
| `live_tv` | 3 | 3 | 2044, 2583, 4054 |
| `myPreferencesMenuPage` | 3 | 3 | 421, 4802, 5114 |
| `playerStats` | 3 | 3 | 6046, 7682, 7718 |
| `readOnlyContent` | 3 | 3 | 4062, 6157, 6811 |
| `sectionTitle-cards` | 3 | 3 | 1783, 5183, 5243 |
| `sectionTitleContainer` | 3 | 3 | 1815, 1873, 5032 |
| `itemExternalLinks` | 13 | 2 | 3173–3251, 3402 |
| `mdl-slider` | 11 | 2 | 2954, 3009–3084 |
| `checkboxOutline` | 10 | 2 | 3575–3616, 3647–3677 |
| `itemBackdrop` | 9 | 2 | 2010–2069, 2257 |
| `cardOverlayButton-br` | 8 | 2 | 1057, 1086–1137 |
| `detail-clamp-text` | 7 | 2 | 3338–3364, 3390–3394 |
| `divUsers` | 7 | 2 | 6168–6172, 7409–7436 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3612–3616, 3646–3665 |
| `countIndicator` | 6 | 2 | 804–834, 7682–7706 |
| `detailPagePrimaryContainer` | 6 | 2 | 1634–1676, 2490 |
| `detailsGroupItem` | 6 | 2 | 4855, 4926–4963 |
| `headerLeft` | 6 | 2 | 1733–1770, 6916 |
| `selectionCommandsPanel` | 6 | 2 | 3532–3566, 7611 |
| `trackSelections` | 6 | 2 | 4824–4855, 4991–4996 |
| `withBackdrop` | 6 | 2 | 2662, 2703–2721 |
| `detailSection` | 5 | 2 | 4811–4820, 4976–4996 |
| `emby-textarea` | 5 | 2 | 5531–5550, 5578–5596 |
| `fullSyncIndicator` | 5 | 2 | 804–827, 7682–7706 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3133, 7322–7339 |
| `manualLoginForm` | 5 | 2 | 6139–6183, 6224 |
| `mediaInfoItem` | 5 | 2 | 1887–1930, 7199 |
| `overview-expand` | 5 | 2 | 3370–3394, 4893 |
| `scrollX` | 5 | 2 | 1788, 1826–1846 |
| `videoIndicator` | 5 | 2 | 3721–3749, 7682 |
| `visualLoginForm` | 5 | 2 | 6139–6183, 6224 |
| `withSectionTabs` | 5 | 2 | 2712–2729, 6538 |
| `alphaPickerButton` | 4 | 2 | 674, 5047–5059 |
| `emby-select` | 4 | 2 | 5540–5561, 7748 |
| `emby-tab-button-active` | 4 | 2 | 3994, 6764–6778 |
| `mediaSourceIndicator` | 4 | 2 | 804–827, 7682 |
| `play_arrow` | 4 | 2 | 3758–3774, 3961 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4625–4630, 6387–6393 |
| `programCell` | 4 | 2 | 5813, 5872–5881 |
| `cardOverlayButtonIcon` | 3 | 2 | 1057–1069, 1137 |
| `castCollapsible` | 3 | 2 | 866, 3616–3625 |
| `detailPageSecondaryContainer` | 3 | 2 | 1655–1680, 1805 |
| `emby-scrollbuttons-button` | 3 | 2 | 1877, 7983–7990 |
| `guestCastContent` | 3 | 2 | 866, 3616–3625 |
| `guide-channelHeaderCell` | 3 | 2 | 674, 5847–5863 |
| `guide-date-tab-button` | 3 | 2 | 674, 3994–4002 |
| `headerUserButton` | 3 | 2 | 594–607, 5118 |
| `noHeaderRight` | 3 | 2 | 1703, 6068–6072 |
| `overview` | 3 | 2 | 3390–3394, 4903 |
| `add` | 2 | 2 | 1788, 7199 |
| `alphaPicker-fixed-right` | 2 | 2 | 2753, 5059 |
| `backdropImageFadeIn` | 2 | 2 | 2818, 7722 |
| `book` | 2 | 2 | 2044, 2583 |
| `btnDeleteImage` | 2 | 2 | 3778, 4008 |
| `cardContent` | 2 | 2 | 866, 898 |
| `cardOverlayButton` | 2 | 2 | 1071, 1114 |
| `cardOverlayButton-hover` | 2 | 2 | 958, 1086 |
| `chevron_right` | 2 | 2 | 5213, 5255 |
| `classList` | 2 | 2 | 1788, 7199 |
| `collapseContent` | 2 | 2 | 3527, 4018 |
| `collectionItemsContainer` | 2 | 2 | 1815, 5036 |
| `content-primary` | 2 | 2 | 5100, 5149 |
| `editorsChoiceContainer` | 2 | 2 | 6872, 7901 |
| `editorsChoiceItemBanner` | 2 | 2 | 6872, 7630 |
| `editorsChoiceItemOverview` | 2 | 2 | 7901, 7994 |
| `endsAt` | 2 | 2 | 1908, 7199 |
| `f5f5f5` | 2 | 2 | 5365, 5404 |
| `fieldDescription` | 2 | 2 | 314, 7748 |
| `formDialogFooter-clear` | 2 | 2 | 3522, 4020 |
| `guide-programNameCaret` | 2 | 2 | 314, 5829 |
| `headroom` | 2 | 2 | 6526, 6563 |
| `indicator` | 2 | 2 | 834, 3709 |
| `mc-row` | 2 | 2 | 462, 7522 |
| `mediaInfoOfficialRating` | 2 | 2 | 1908, 7199 |
| `navMenuOption-selected` | 2 | 2 | 4807, 7333 |
| `nowPlayingInfoContainer` | 2 | 2 | 3164, 6324 |
| `org` | 2 | 2 | 3200, 3230 |
| `page` | 2 | 2 | 2753, 7103 |
| `paperList` | 2 | 2 | 875, 4031 |
| `playlist` | 2 | 2 | 4620, 6302 |
| `programSecondaryTitle` | 2 | 2 | 314, 5881 |
| `queue` | 2 | 2 | 2044, 2583 |
| `reactRoot` | 2 | 2 | 4496, 6922 |
| `recordingFields` | 2 | 2 | 4847, 4991 |
| `runtime` | 2 | 2 | 6236, 6264 |
| `sectionTitleContainer-cards` | 2 | 2 | 5178, 5243 |
| `sidebarHeader` | 2 | 2 | 4158, 7339 |
| `splide` | 2 | 2 | 6872, 7950 |
| `tagline` | 2 | 2 | 2653, 4903 |
| `upNextDialog-title` | 2 | 2 | 5295, 5329 |
| `vertical-list` | 2 | 2 | 1850, 7849 |
| `vertical-wrap` | 2 | 2 | 800, 1815 |
| `videoOsdBottom` | 2 | 2 | 3156, 6493 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3156, 6493 |
| `userPreferencesPage` | 12 | 1 | 7733–7829 |
| `checkboxContainer` | 7 | 1 | 3604–3641 |
| `itemDetailsGroup` | 7 | 1 | 4910–4996 |
| `itemProgressBar` | 6 | 1 | 2868–2902 |
| `streaming-lookup-container` | 6 | 1 | 3258–3303 |
| `trackSelectionFieldContainer` | 6 | 1 | 4866–4889 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7950–7990 |
| `emby-select-withcolor` | 5 | 1 | 5540–5604 |
| `innerCardFooter` | 5 | 1 | 3417–3446 |
| `chapterCardImageContainer` | 4 | 1 | 3417–3446 |
| `endTimeText` | 4 | 1 | 6236–6264 |
| `mainDetailButtons` | 4 | 1 | 3957–3971 |
| `overview-controls` | 4 | 1 | 3390–3402 |
| `startTimeText` | 4 | 1 | 6236–6258 |
| `backgroundProgress` | 3 | 1 | 2879–2891 |
| `button-flat` | 3 | 1 | 3137–3147 |
| `cardIndicators` | 3 | 1 | 3694–3704 |
| `cardOverlayFab-primary` | 3 | 1 | 1049–1071 |
| `com` | 3 | 1 | 3206–3224 |
| `content` | 3 | 1 | 4932–4963 |
| `fab` | 3 | 1 | 3798–3811 |
| `listChildrenCollapsible` | 3 | 1 | 4981–4996 |
| `mdl-slider-background-flex` | 3 | 1 | 2978–2991 |
| `mediaInfoCriticRating` | 3 | 1 | 1949–1958 |
| `nextUpSection` | 3 | 1 | 4976–4996 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6288–6298 |
| `playbackProgress` | 3 | 1 | 2879–2891 |
| `serverInfo` | 3 | 1 | 4035–4044 |
| `transcodingProgress` | 3 | 1 | 2879–2891 |
