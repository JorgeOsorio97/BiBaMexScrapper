import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd


driver = webdriver.Chrome("/home/jorge-valdez/chromedriver")
driver.get('https://picomponentebi.cnbv.gob.mx/ReportViwer/ReportService?sector=40&tema=2&subTema=3&tipoInformacion=0&subTipoInformacion=0&idReporte=040_11q_BIPER0&idPortafolio=0&idTipoReporteBI=1')
# driver.get('https://picomponentebi.cnbv.gob.mx/ReportViwer/ReportService?sector=68&tema=2&subTema=3&tipoInformacion=0&subTipoInformacion=0&idReporte=068_11q_BIPER0&idPortafolio=0&idTipoReporteBI=1')
ifm = driver.find_element_by_xpath('//iframe')


def sleep_wf(segs, message=None):
    if message:
        print(message)
    for i in range(segs):
        print(i)
        time.sleep(1)


sleep_wf(20)
# driver.implicitly_wait(10)
boton_filtros = driver.find_element_by_xpath(
    '//button[@id="btn_OcultaFiltros"]').click()
sleep_wf(5)
# driver.implicitly_wait(10)
driver.find_element_by_xpath(
    '//input[@id="rbdIntervalo1" and @value="14"]').click()

meses_list = driver.find_elements_by_xpath(
    '//label[./input[@type="checkbox" and @class="chk_Box_Val" and starts-with(@value,"[Periodos]")]]')
# print(meses_list)
print("Numero de meses posibles", len(meses_list))

driver.find_element_by_xpath('//h3[@id="Institucion_6_H"]').click()

instituciones_list = driver.find_elements_by_xpath(
    '//label[./input[@type="checkbox" and @class="chk_Box_Val" and starts-with(@value,"[Instituciones]")]]')
print("Numero de instituciones", len(instituciones_list))


# Limpiar listas a Dicts
meses_list = [{"nombre": mes.find_element_by_tag_name(
    'input').get_attribute('id')[-6:], 'valor':mes.find_element_by_tag_name(
    'input').get_attribute('value'), 'id':mes.find_element_by_tag_name(
    'input').get_attribute('id')} for mes in meses_list]

instituciones_list = [{"nombre": inst.text, 'valor': inst.find_element_by_tag_name(
    'input').get_attribute('value'), 'id': inst.find_element_by_tag_name(
    'input').get_attribute('id')} for inst in instituciones_list]

# print(meses_list)

df = pd.DataFrame(data=meses_list+instituciones_list,
                  columns=['nombre', 'valor', 'id'])

df.to_csv('test.csv')

result_df = pd.DataFrame(
    [], columns=['nombre_p', 'valor_p', 'id_p', 'nombre_in', 'valor_in', 'id_in'])

driver.find_element_by_xpath('//h3[@id="Escala_3_H"]').click()
sleep_wf(1)
driver.find_element_by_xpath('//input[@id="rdbEscala1"]').click()
sleep_wf(1)
driver.find_element_by_xpath('//button[@id="btn_GeneraRoporte"]').click()

sleep_wf(15)
for mes_i, mes in enumerate(meses_list):
    for inst_i, inst in enumerate(instituciones_list):

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "btn_OcultaFiltros"))
        )
        sleep_wf(1, "Boton Mostrat Filtros")
        # Mostrar filtros
        driver.find_element_by_xpath(
            '//button[@id="btn_OcultaFiltros"]').click()

        sleep_wf(2, "Filtrar: Configurar Periodos")
        # PERIODOS
        # Abrir Periodos
        driver.find_element_by_xpath('//h3[@id="Periodo_Filtros_H"]').click()
        # Definir configurar consulta
        sleep_wf(1)
        driver.find_element_by_xpath(
            '//input[@id="rbdIntervalo1" and @value="14"]').click()

        sleep_wf(1)

        # SELECCIONAR PERIODO
        driver.find_element_by_xpath('//h3[@id="Periodo_5_H"]').click()
        if mes_i != 0:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, mes['id']))
            )
            sleep_wf(1, "Seleccionar meses")
            driver.find_element_by_xpath(
                '//input[@id="{}"]'.format(meses_list[0]['id'])).click()
            sleep_wf(1)
            driver.find_element_by_xpath(
                '//input[@id="{}"]'.format(mes['id'])).click()

        sleep_wf(1, 'Seleccionar Instituciones')

        # INSTITUCIONES
        driver.find_element_by_xpath('//h3[@id="Institucion_6_H"]').click()
        if inst_i != 0:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, inst['id']))
            )
            sleep_wf(1)
            driver.find_element_by_xpath(
                '//input[@id="{}"]'.format(instituciones_list[0]['id'])).click()
            sleep_wf(1)
            driver.find_element_by_xpath(
                '//input[@id="{}"]'.format(inst['id'])).click()

        sleep_wf(1)

        print(mes['nombre'], mes['valor'], mes['id'])
        print(inst['nombre'], inst['valor'], inst['id'])

        driver.find_element_by_xpath('//h3[@id="Escala_3_H"]').click()
        sleep_wf(1)
        driver.find_element_by_xpath('//input[@id="rdbEscala1"]').click()
        sleep_wf(1)
        driver.find_element_by_xpath(
            '//button[@id="btn_GeneraRoporte"]').click()

        sleep_wf(15, "Primer iframe")

        # Descargar como csv
        # Cambiamos de iframe
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, mes['IFrame_Container']))
        )
        frames_list = driver.find_elements_by_tag_name('iframe')
        sleep_wf(1, "Segundo iframe")
        frame1 = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(frame1)
        frames_list = driver.find_elements_by_tag_name('iframe')
        frame2 = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(frame2)
        driver.implicitly_wait(5)
        driver.find_element_by_id(
            'ReportViewer1_ctl05_ctl04_ctl00_ButtonLink').click()
        # driver.find_element_by_css_selector(
        #     'a#ReportViewer1_ctl05_ctl04_ctl00_ButtonLink').click
        # driver.find_element_by_xpath(
        #     '//a[@id="ReportViewer1_ctl05_ctl04_ctl00_ButtonLink"]').click()
        driver.find_element_by_xpath(
            '//a[@title="CSV (delimitado por comas)"]').click()

        sleep_wf(5)
        driver.implicitly_wait(20)
        driver.get('https://picomponentebi.cnbv.gob.mx/ReportViwer/ReportService?sector=40&tema=2&subTema=3&tipoInformacion=0&subTipoInformacion=0&idReporte=040_11q_BIPER0&idPortafolio=0&idTipoReporteBI=1')

        temp_df = pd.DataFrame(
            [[mes['nombre'], mes['valor'], mes['id'], inst['nombre'], inst['valor'], inst['id']]], columns=['nombre_p', 'valor_p', 'id_p', 'nombre_in', 'valor_in', 'id_in'])
        result_df.append(temp_df, ignore_index=True)
        result_df.to_csv('result.csv')
        sleep_wf(30)

result_df.to_csv('result.csv')
