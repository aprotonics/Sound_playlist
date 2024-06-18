from selenium.webdriver.common.by import By


# Main page
close_button_selector = (By.CSS_SELECTOR, '.pay-promo-close-btn span')
auth_button_selector = (By.CSS_SELECTOR, 'a.log-in')
playlists_button_selector = (By.CSS_SELECTOR, '.nav-kids .nav-kids__tab:nth-child(4) a')

# Auth page
auth_form_selector = (By.CSS_SELECTOR, '.passp-auth')
layout_content_selector = (By.CSS_SELECTOR, '.layout_content')
authLoginInputToggle_selector = (By.CSS_SELECTOR, '.AuthLoginInputToggle-wrapper')
authLoginInputToggle_input_selector = (By.CSS_SELECTOR, '.AuthLoginInputToggle-input')
authLoginInputToggle_loginField_selector = (By.CSS_SELECTOR, '.AuthLoginInputToggle-loginField')
field_inputWrapper_selector = (By.CSS_SELECTOR, '.Field-inputWrapper')
textinput_selector = (By.CSS_SELECTOR, '.Textinput')
textinput_Control_selector = (By.CSS_SELECTOR, '.Textinput-Control')

sign_in_button1_selector = (By.CSS_SELECTOR, '.Button2_type_submit')
sign_in_button2_selector = (By.CSS_SELECTOR, 'button.Button2_type_submit')

# Playlists page
tracks_button_selector = (By.CSS_SELECTOR, '.d-tabs .d-tabs__tab:nth-child(1) a')

# Tracks page
d_track__start_column_selector = (By.CSS_SELECTOR, '.d-track__start-column')
d_subhead__title_main_selector = (By.CSS_SELECTOR, 'span.d-subhead__title-main')
d_track__info_selector = (By.CSS_SELECTOR, '.d-track__info span')

tracks_titles_selector = (By.CSS_SELECTOR, '.d-track')
track_title_selector = (By.CSS_SELECTOR, '.d-track__name')
track_menu_selector = (By.CSS_SELECTOR, '.d-context-menu span')
track_menu_tab_selector = (By.CSS_SELECTOR, '.d-context-menu__tab_main')
track_menu_tab_item_selector = (By.CSS_SELECTOR, 'ul li:nth-child(3) span.d-context-menu__item-icon span')
track_menu_tab2_selector = (By.CSS_SELECTOR, '.d-context-menu__tab')
track_menu_playlist_to_add_selector = (
                                        By.CSS_SELECTOR, 
                                       '.d-addition__playlists .d-addition__item:nth-child(2) span.d-addition__item-text'
                                       )





















# Filter page
products_general_selector = (By.XPATH, '//div[contains(@class, "grid__product")]/div')
products_prices_selector = (By.XPATH, '//*[contains(@class, "ec-price-item")]')
low_price_selector = (By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[1]')
high_price_selector = (By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[2]')
filters_count_selector = (By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]')
products_container_selector = (By.XPATH, '//div[contains(@class, "grid__products")]')
first_product_selector = (By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')
products_filtered_selector = (By.XPATH, '//div[contains(@class, "grid__product")]/div')
products_names_selelctor = (By.XPATH, '//div[contains(@class, "grid-product__title-inner")]')
filter_by_in_stock_checkbox_selector = (By.XPATH, '//*[@id="checkbox-in_stock"]')
filter_by_discount_checkbox_selector = (By.XPATH, '//*[@id="checkbox-on_sale"]')

# Sort page
filters_selector = (By.XPATH, '//div[contains(@class, "ec-filter--search")]')
products_titles_selector = (By.XPATH, '//div[contains(@class, "grid-product__title-inner")]')
products_prices_selector = (By.XPATH, '//div[contains(@class, "grid-product__price-value")]')
product_sort_selector = (By.XPATH, '//*[@id="ec-products-sort"]')

# Main page
search_button_selector = (By.CSS_SELECTOR, '#static-html a.footer__link--all-products')

# Search page
filters_selector = (By.CSS_SELECTOR, '.ec-filters__wrap .ec-filter--offers .form-control__inline-label')
product_prices_selector = (By.CSS_SELECTOR, '.grid__products .grid-product .grid-product__price-value')

# Product page
cart_button_selector = (By.CSS_SELECTOR, '.details-product-purchase__add-buttons .form-control:last-child button.form-control__button')
cart_span_selector = (By.CSS_SELECTOR, '.details-product-purchase__add-buttons .form-control:last-child button.form-control__button span.form-control__button-text')
cart_icon_selector = (By.CSS_SELECTOR, '.float-icons__icon--cart > .ec-cart-widget > .ec-minicart')

# Cart page
email_input_selector = (By.CSS_SELECTOR, '#ec-cart-email-input')
checkbox_agree_selector = (By.CSS_SELECTOR, '#form-control__checkbox--agree')
place_order_button_selector = (By.CSS_SELECTOR, '.form-control__button > .form-control__loader')

# Checkout page
name_input_selector = (By.CSS_SELECTOR, '#ec-full-name')
address_input_selector = (By.CSS_SELECTOR, '#ec-address-line1')
city_input_selector = (By.CSS_SELECTOR, '#ec-city-list')
postal_input_selector = (By.CSS_SELECTOR, '#ec-postal-code')
place_order_button2_selector = (By.CSS_SELECTOR, '.form-control__button > .form-control__loader')

# Order confirm page
thanks_block_selector = (By.CSS_SELECTOR, 'div.ec-store__confirmation-page h1.page-title__name')
