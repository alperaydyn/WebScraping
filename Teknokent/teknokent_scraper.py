from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import requests
from bs4 import BeautifulSoup
import json

# https://www.roelpeters.be/how-to-deploy-a-scraping-script-and-selenium-in-google-cloud-run/

class BilisimVadisi():
    
    def __init__(self):
        self.wdm = ChromeDriverManager().install()
        print('Bilisim Vadisi scraper initialized')
    
    def test(self):
        return [
         ('10X Bilişim A.Ş', 'https://10xbilisim.com/'),
         ('20H2O Teknoloji', 'https://www.20h2oinvest.com/'),
         ('Ağahan OSGB', 'http://www.agahanosgb.com/'),
         ('Ahicommerce', 'https://www.ahicommerce.com/'),
         ('Aktif', 'https://aktif.net/'),
         ('Albert Solino', 'https://www.albertsolino.com/'),
         ('Anibal Bilişim', 'https://anibalbilisim.com/'),
         ('Ardem Yazılım', 'http://ardemyazilim.com/'),
         ('Argenova', 'https://www.argenova.com.tr/'),
         ('Argetip', 'http://www.argetip.com/'),
         ('Armada Yazılım', 'https://www.armadayazilim.com/'),
         ('Asb Yazılım', 'http://www.asbyazilim.com.tr/'),
         ('ASELSAN', 'https://www.aselsan.com.tr/'),
         ('Atak Robot', 'https://atakrobot.com.tr/'),
         ('AugeLab', 'https://augelab.com/'),
         ('Ayasofyazılım', 'https://www.ayasofyazilim.com/'),
         ('Aybit Teknoloji A.Ş', 'https://www.aybit.com.tr/'),
         ('Bahacan', 'http://www.bahacan.com/'),
         ('beeNEO', 'https://www.beeneo.com/'),
         ('Bevese', 'https://bevese.com/'),
         ('Bilet Dükkanı', 'https://www.biletdukkani.com/'),
         ('Bilisim112', 'https://bilisim112.com/'),
         ('Biset Yazılım', 'http://www.bisetyazilim.com/'),
         ('BM TECH', 'http://www.bmtech.com.tr/'),
         ('BrandZone', 'https://www.brandzone.com.tr/'),
         ('CDMMobil', 'https://www.cdmmobil.com.tr/'),
         ('Coconut Game', 'http://www.coconutgame.com/'),
         ('CTcomm', 'https://www.ctcomm.com.tr/'),
         ('Daiichi', 'https://www.daiichi.com/'),
         ('diji tohum', 'https://www.dijitohum.com.tr/'),
         ('Dijital Kurye', 'https://dijitalkurye.com.tr/'),
         ('Dizen Motor', 'https://www.dizenmotor.com.tr/'),
         ('Duman R&D', 'https://www.dumanarge.com/'),
         ('Düşyeri', 'https://www.dusyeri.com/'),
         ('DVU', 'https://www.dvu.com.tr/'),
         ('E-Halı Servisi', 'https://www.e-haliservisi.com/'),
         ('EDAG', 'https://tr.edag.com/'),
         ('Ege Kariyer', 'http://www.egekariyer.com/'),
         ('Eksera', 'https://eksera.com/'),
         ('Elta', 'https://elta360.com/'),
         ('Entechno', 'http://entechno.com.tr/'),
         ('Erkba', 'https://erkba.com/'),
         ('Fabrikod', 'https://www.fabrikod.com/'),
         ('Faraday', 'https://faraday.net/'),
         ('FEV', 'https://www.fev.com/'),
         ('FHT Yazılım', 'http://fhtyazilim.com/'),
         ('Geobilgi', 'https://www.geobilgi.com/'),
         ('Gir-in', 'https://www.gir-in.com/'),
         ('Goart Metaverse', 'https://www.goartmetaverse.com/'),
         ('Guru Teknoloji', 'https://www.gurutek.com.tr/'),
         ('Hamle Mühendislik', 'https://hamlemuhendislik.com/'),
         ('HAN Spaces', 'https://www.hanspaces.com/'),
         ('Happy Crab Game Studio', 'https://www.happycrab.com.tr/'),
         ('HAVELSAN', 'https://www.havelsan.com.tr/'),
         ('HeyMobility', 'https://heymobility.tech/'),
         ('Hipposoft', 'https://www.hipposoft.net/'),
         ('Infinity e-learning', 'https://infinityelearning.com/'),
         ('inotion', 'https://inotion.co/'),
         ('Internative', 'https://internative.net/'),
         ('İpucu Bilişim', 'http://www.ipucubilisim.com.tr/'),
         ('İstanbulAI', 'https://istanbulai.com/'),
         ('Kitslo', 'https://kitslo.com/'),
         ('Kodris', 'https://www.kodris.com/'),
         ('Kronnika', 'https://kronnika.com/'),
         ('Kuantek', 'http://www.kuantek.com.tr/'),
         ('Kumbara', 'https://www.kumbarateknoloji.com/'),
         ('Letta Grup', 'https://www.letta.com.tr/'),
         ('Lion Yazılı ve Enerji A.Ş.', 'https://sistemlion.com/'),
         ('Mahrek Teknoloji', 'https://www.mahrek.com.tr/'),
         ('Megisty Teknoloji', 'https://www.megisty.com/'),
         ('Metin Madenciliği', 'http://www.metinmadencisi.com/'),
         ('Miafon', 'https://miafon.com.tr/'),
         ('Miltera', 'https://miltera.com.tr/'),
         ('Mina', 'http://www.minapy.com.tr/'),
         ('Mirengi', 'https://www.mirengi.com.tr/'),
         ('Mirket Security', 'https://www.mirketsecurity.com/'),
         ('MobileITM', 'https://mobileitm.com/'),
         ('Mr.Holo', 'https://mrholo.co/'),
         ('MRZ', 'https://www.kompostsistem.com/'),
         ('Natustech', 'https://www.natustech.com/'),
         ('Netsum', 'http://www.netsum.com.tr/'),
         ('niocycle', 'https://niocycle.com/'),
         ('Nordtek Green', 'http://www.nordtekgreen.com/'),
         ('Novacon', 'http://novacon.com.tr/'),
         ('Novelty', 'https://noveltybilisim.com.tr/'),
         ('Odak İnovasyon', 'http://www.odakinovasyon.com.tr/'),
         ('Odyssey Yazılım', 'http://odyssey.com.tr/'),
         ('omChain', 'https://omchain.io/'),
         ('OrganiCompost', 'https://orcomtech.com/'),
         ('Orka Tech', 'https://www.yukal.net/'),
         ('Ortem', 'https://www.ortem.com.tr/'),
         ('Oskon Otomasyon', 'http://www.oskonotomasyon.com.tr/'),
         ('Oto Kiosk', 'https://otokiosk.com/'),
         ('Panod', 'https://panod.eu/'),
         ('PATH', 'https://path.com.tr/'),
         ('Pavotek', 'https://www.pavotek.com.tr/'),
         ('Pineasoft', 'http://www.pineasoft.com/'),
         ('Prodemo', 'https://www.prodemo.com.tr/'),
         ('Protek Saglık', 'https://proteksaglik.com/'),
         ('Pulur Teknoloji', 'http://www.pulur.com.tr/'),
         ('QualisICT', 'https://www.qualisict.com/'),
         ('Rakis Yapay Zeka', 'https://www.rakis.com.tr/'),
         ('Rapunzel', 'https://rapunzel.app/'),
         ('RBTWIN', 'https://robo.com.tr/sayfa/rbtwin-mes.html'),
         ('RDC+', 'https://rdc.plus/'),
         ('Remergen', 'https://www.remergen.com/'),
         ('RINNOVA', 'https://www.rinnovatech.com/'),
         ('Ritma', 'https://www.ritma.com.tr/'),
         ('Robo Otomasyon', 'https://robo.com.tr/'),
         ('Roof Stacks', 'https://roofstacks.com/'),
         ('Sadede Gel', 'http://sadedegel.com/'),
         ('Sagita', 'http://sagita.com.tr/'),
         ('Sanai', 'https://www.sanai.com.tr/'),
         ('Saykal Electronics', 'https://saykal.com/'),
         ('Seyir Mobil Sistemler', 'https://www.seyirmobil.com/'),
         ('Sintel', 'https://sintel.com.tr/'),
         ('Smartclass', 'https://www.smartclass.com.tr/'),
         ('Smartface', 'https://smartface.io/'),
         ('Softrue', 'http://www.softrue.com.tr/'),
         ('Sonicmob', 'http://sonicmob.co/'),
         ('Teira3D', 'https://www.teira3d.com/'),
         ('Tekno Kurgu', 'http://www.teknokurgu.com.tr/'),
         ('Togg', 'https://www.togg.com.tr/'),
         ('Turmach', 'https://www.turmach.com/'),
         ('VAGA', 'https://www.vagani.com/'),
         ('Valven', 'https://www.valven.com/'),
         ('Veribox', 'https://www.veribox.com.tr/'),
         ('Viral Yazılım', 'https://viralyazilim.com/'),
         ('Visiobit', 'http://visiobit.com/'),
         ('VNGTECH', 'https://vngtech.com/'),
         ('Waa2', 'https://www.waa2.com/'),
         ('Wabi Digital', 'https://www.wabidigital.com/'),
         ('Werer Group', 'https://werergroup.com/'),
         ('Wiser', 'https://wiserchip.com/'),
         ('Yankı Solutions', 'https://www.yankisolutions.com/'),
         ('Yonca Bilişim Teknolojileri', 'http://www.yoncabt.com.tr/'),
         ('Yükal', 'https://www.yukal.net/'),
         ('ZUKOD Yazılım', 'https://www.zukod.com.tr/')]
    
    def run(self):
        #return self.wdm
    
        #driver = webdriver.Chrome(service=Service(self.wdm))
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        url = "https://bilisimvadisi.com.tr/hakkimizda/firmalar/"
        driver.get(url)
        driver.implicitly_wait(5)

        privacy_button = driver.find_element(By.CLASS_NAME,'fusion-privacy-bar-acceptance')
        privacy_button.click()

        div = driver.find_elements(By.CLASS_NAME, "ex-loadmore")
        btn = driver.find_elements(By.CLASS_NAME, "load-text")
        print('start fetching')
        while div:
            driver.implicitly_wait(5)
            div = driver.find_elements(By.CLASS_NAME, "ex-loadmore")
            btn = driver.find_elements(By.CLASS_NAME, "load-text")
            #actions = ActionChains(driver)
            #actions.move_to_element(btn[-1]).perform()


            if not btn:
                print('> completed')
                break
            try:
                div[-1].click()
                #actions.click(btn[-1])
                print('.', end='')
            except Exception as ex:
                print('\nHata:', ex)
                break

        firms = driver.find_elements(By.CLASS_NAME, "item-grid")
        firms = [(divf.text, divf.find_element(By.TAG_NAME, "a").get_attribute('href')) for divf in firms]
        return firms
    
class Kapadokya():
    def __init__(self):
        print('Kapadokya Teknokent')
        
    def run(self):
        return None
    
class Bogazici():
    def __init__(self):
        print('Boğaziçi Teknokent')
        
    def run(self):
        url = 'http://teknopark.boun.edu.tr/?q=sirketler'
        req = requests.get(url)
        soup = BeautifulSoup(req.content,"html.parser")
        div = soup.find('div', class_='sirketler')
        sirketler = div.find_all('span')
        
        sirketler = [
            (sirket.find('span', class_='sirket_adi').text.strip(), 
             sirket.find('a').text.strip() if sirket.find('a') else ''
            ) 
            for sirket in div.find_all('li')
        ]
        return sirketler
    
class Cumhuriyet():
    def __init__(self):
        print('Cumhuriyet Teknopark')
        
    def run(self):
        url ='https://www.cumhuriyetteknokent.com/firmalar?'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        req = requests.get(url, headers = headers)
        soup = BeautifulSoup(req.content)
        divs = soup.find('div', id='blog').find_all('div', class_='post-item')
        sirketler = [(d.find('h5').text, d.find('a')['href'] if d.find('a') else '') for d in divs]
        
        return sirketler
    
class Duzce():
    def __init__(self):
        print('Düzce Teknopark')
    
    def run(self):
        url1 = 'https://www.duzceteknopark.com/firmalar?action=jet_engine_ajax&handler=get_listing&page_settings%5Bpost_id%5D=737&page_settings%5Bqueried_id%5D=2745%7CWP_Post&page_settings%5Belement_id%5D=91825b6&page_settings%5Bpage%5D=1&listing_type=elementor&isEditMode=false'
        url2 = 'https://www.duzceteknopark.com/firmalar?action=jet_engine_ajax&handler=listing_load_more&query%5Bpost_status%5D%5B%5D=publish&query%5Bpost_type%5D=firmalar&query%5Bposts_per_page%5D=100&query%5Bpaged%5D=1&query%5Bignore_sticky_posts%5D=1&query%5Bsuppress_filters%5D=false&query%5Bjet_smart_filters%5D=jet-engine%2Fdefault&widget_settings%5Blisitng_id%5D=709&widget_settings%5Bposts_num%5D=26&widget_settings%5Bcolumns%5D=4&widget_settings%5Bcolumns_tablet%5D=3&widget_settings%5Bcolumns_mobile%5D=1&widget_settings%5Bis_archive_template%5D=&widget_settings%5Bpost_status%5D%5B%5D=publish&widget_settings%5Buse_random_posts_num%5D=&widget_settings%5Bmax_posts_num%5D=9&widget_settings%5Bnot_found_message%5D=Firma+bulunamad%C4%B1...&widget_settings%5Bis_masonry%5D=false&widget_settings%5Bequal_columns_height%5D=yes&widget_settings%5Buse_load_more%5D=yes&widget_settings%5Bload_more_id%5D=&widget_settings%5Bload_more_type%5D=scroll&widget_settings%5Bload_more_offset%5D%5Bunit%5D=px&widget_settings%5Bload_more_offset%5D%5Bsize%5D=0&widget_settings%5Buse_custom_post_types%5D=&widget_settings%5Bhide_widget_if%5D=&widget_settings%5Bcarousel_enabled%5D=&widget_settings%5Bslides_to_scroll%5D=1&widget_settings%5Barrows%5D=true&widget_settings%5Barrow_icon%5D=fa+fa-angle-left&widget_settings%5Bdots%5D=&widget_settings%5Bautoplay%5D=true&widget_settings%5Bautoplay_speed%5D=5000&widget_settings%5Binfinite%5D=true&widget_settings%5Bcenter_mode%5D=&widget_settings%5Beffect%5D=slide&widget_settings%5Bspeed%5D=500&widget_settings%5Binject_alternative_items%5D=&widget_settings%5Bscroll_slider_enabled%5D=&widget_settings%5Bscroll_slider_on%5D%5B%5D=desktop&widget_settings%5Bscroll_slider_on%5D%5B%5D=tablet&widget_settings%5Bscroll_slider_on%5D%5B%5D=mobile&widget_settings%5Bcustom_query%5D=false&widget_settings%5Bcustom_query_id%5D=&widget_settings%5B_element_id%5D=&page_settings%5Bpost_id%5D=false&page_settings%5Bqueried_id%5D=false&page_settings%5Belement_id%5D=false&page_settings%5Bpage%5D=1&listing_type=false&isEditMode=false'
        #print(url2.replace('%5B','[').replace('%5D',']').replace('&','\n'))
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        # read content, no need to parse with Beautifulsoup, response is json
        req = requests.get(url2, headers = headers)
        
        # retrieve html attribute from content
        jd = json.loads(req.content)
        
        # parse html part with BS
        soup = BeautifulSoup(jd['data']['html'])
        
        divs = soup.find_all('section')
        sirketler = [
            (d.find('span', class_='jet-listing-dynamic-link__label').text.strip(), d.find('a')['href'])
            for d in divs
        ]
        
        return sirketler
        
        
        