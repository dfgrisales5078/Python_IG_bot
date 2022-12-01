def comment_on_posts(self) -> None:
    comment_box_path = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea '
    comment_box = self.browser.find_element(
        By.XPATH, comment_box_path)
    comment_box.send_keys('Niceeeeeeee')
    sleep(1)

    post_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button '
    post = self.browser.find_element(
        By.XPATH, post_xpath)
    post.click()
    sleep(1)
