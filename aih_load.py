import config
from elasticsearch import Elasticsearch

params = config.config()
print(params)

elastic_user = params['user']
elastic_pass = params['pass']
elastic_host = params['host']

es = Elasticsearch(
        ['' + elastic_host  + ''], 
        http_auth=('' + elastic_user  + '', '' + elastic_pass  + ''),
        scheme="https",
        verify_certs=True)
print('Connected elasticsearch...')
print(es.info())

indice= "datasus-sih"
doc_type="sih-type"
try :
    es.indices.delete(index=indice)
except :
    pass

sih_type = {
                "settings" : {
                    "number_of_shards" : 1
                },
                "mappings":{
                        'properties': {
                                  'ANO_CMPT': {
                                    'type': 'long'
                                  },
                                  'AUD_JUST': {
                                    'type': 'keyword'
                                  },
                                  'CAR_INT': {
                                    'type': 'long'
                                  },
                                  'CBOR': {
                                    'type': 'keyword'
                                  },
                                  'CEP': {
                                    'type': 'long'
                                  },
                                  'CGC_HOSP': {
                                    'type': 'keyword'
                                  },
                                  'CID_ASSO': {
                                    'type': 'keyword'
                                  },
                                  'CID_MORTE': {
                                    'type': 'keyword'
                                  },
                                  'CID_NOTIF': {
                                    'type': 'keyword'
                                  },
                                  'CNAER': {
                                    'type': 'long'
                                  },
                                  'CNES': {
                                    'type': 'long'
                                  },
                                  'CNPJ_MANT': {
                                    'type': 'float'
                                  },
                                  'INFEHOSP': {
                                    'type': 'keyword'
                                  },
                                  'COBRANCA': {
                                    'type': 'long'
                                  },
                                  'COD_IDADE': {
                                    'type': 'long'
                                  },
                                  'COMPLEX': {
                                    'type': 'long'
                                  },
                                  'CONTRACEP1': {
                                    'type': 'long'
                                  },
                                  'CONTRACEP2': {
                                    'type': 'long'
                                  },
                                  'DIAGSEC1': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC2': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC3': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC4': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC5': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC6': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC7': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC8': {
                                    'type': 'keyword'
                                  },
                                  'DIAGSEC9': {
                                    'type': 'keyword'
                                  },
                                  'DIAG_PRINC': {
                                    'type': 'keyword'
                                  },
                                  'DIAG_SECUN': {
                                    'type': 'keyword'
                                  },
                                  'DIAR_ACOM': {
                                    'type': 'long'
                                  },
                                  'DIAS_PERM': {
                                    'type': 'long'
                                  },
                                  'DT_INTER': {
                                    'type': 'long'
                                  },
                                  'DT_SAIDA': {
                                    'type': 'long'
                                  },
                                  'ESPEC': {
                                    'type': 'long'
                                  },
                                  'ETNIA': {
                                    'type': 'long'
                                  },
                                  'FAEC_TP': {
                                    'type': 'float'
                                  },
                                  'FINANC': {
                                    'type': 'long'
                                  },
                                  'GESTAO': {
                                    'type': 'long'
                                  },
                                  'GESTOR_COD': {
                                    'type': 'long'
                                  },
                                  'GESTOR_CPF': {
                                    'type': 'long'
                                  },
                                  'GESTOR_DT': {
                                    'type': 'keyword'
                                  },
                                  'GESTOR_TP': {
                                    'type': 'long'
                                  },
                                  'GESTRISCO': {
                                    'type': 'long'
                                  },
                                  'HOMONIMO': {
                                    'type': 'long'
                                  },
                                  'IDADE': {
                                    'type': 'long'
                                  },
                                  'IDENT': {
                                    'type': 'long'
                                  },
                                  'IND_VDRL': {
                                    'type': 'long'
                                  },
                                  'INSC_PN': {
                                    'type': 'keyword'
                                  },
                                  'INSTRU': {
                                    'type': 'long'
                                  },
                                  'MARCA_UCI': {
                                    'type': 'long'
                                  },
                                  'MARCA_UTI': {
                                    'type': 'long'
                                  },
                                  'MES_CMPT': {
                                    'type': 'long'
                                  },
                                  'MORTE': {
                                    'type': 'long'
                                  },
                                  'MUNIC_MOV': {
                                    'type': 'long'
                                  },
                                  'MUNIC_RES': {
                                    'type': 'long'
                                  },
                                  'NACIONAL': {
                                    'type': 'long'
                                  },
                                  'NUM_PROC': {
                                    'type': 'keyword'
                                  },
                                  'NASC': {
                                    'type': 'long'
                                  },
                                  'NATUREZA': {
                                    'type': 'long'
                                  },
                                  'NAT_JUR': {
                                    'type': 'long'
                                  },
                                  'NUM_FILHOS': {
                                    'type': 'long'
                                  },
                                  'N_AIH': {
                                    'type': 'long'
                                  },
                                  'PROC_REA': {
                                    'type': 'long'
                                  },
                                  'PROC_SOLIC': {
                                    'type': 'long'
                                  },
                                  'QT_DIARIAS': {
                                    'type': 'long'
                                  },
                                  'RACA_COR': {
                                    'type': 'long'
                                  },
                                  'REGCT': {
                                    'type': 'long'
                                  },
                                  'REMESSA': {
                                    'type': 'keyword'
                                  },
                                  'RUBRICA': {
                                    'type': 'long'
                                  },
                                  'SEQUENCIA': {
                                    'type': 'long'
                                  },
                                  'SEQ_AIH5': {
                                    'type': 'long'
                                  },
                                  'SEXO': {
                                    'type': 'long'
                                  },
                                  'SIS_JUST': {
                                    'type': 'keyword'
                                  },
                                  'TOT_PT_SP': {
                                    'type': 'long'
                                  },
                                  'CPF_AUT': {
                                    'type': 'keyword'
                                  },
                                  'TPDISEC1': {
                                    'type': 'long'
                                  },
                                  'TPDISEC2': {
                                    'type': 'long'
                                  },
                                  'TPDISEC3': {
                                    'type': 'long'
                                  },
                                  'TPDISEC4': {
                                    'type': 'long'
                                  },
                                  'TPDISEC5': {
                                    'type': 'long'
                                  },
                                  'TPDISEC6': {
                                    'type': 'long'
                                  },
                                  'TPDISEC7': {
                                    'type': 'long'
                                  },
                                  'TPDISEC8': {
                                    'type': 'long'
                                  },
                                  'TPDISEC9': {
                                    'type': 'long'
                                  },
                                  'UF_ZI': {
                                    'type': 'long'
                                  },
                                  'US_TOT': {
                                    'type': 'float'
                                  },
                                  'UTI_INT_AL': {
                                    'type': 'long'
                                  },
                                  'UTI_INT_AN': {
                                    'type': 'long'
                                  },
                                  'UTI_INT_IN': {
                                    'type': 'long'
                                  },
                                  'UTI_INT_TO': {
                                    'type': 'long'
                                  },
                                  'UTI_MES_AL': {
                                    'type': 'long'
                                  },
                                  'UTI_MES_AN': {
                                    'type': 'long'
                                  },
                                  'UTI_MES_IN': {
                                    'type': 'long'
                                  },
                                  'UTI_MES_TO': {
                                    'type': 'long'
                                  },
                                  'VAL_ACOMP': {
                                    'type': 'float'
                                  },
                                  'VAL_OBSANG': {
                                    'type': 'float'
                                  },
                                  'VAL_ORTP': {
                                    'type': 'float'
                                  },
                                  'VAL_PED1AC': {
                                    'type': 'float'
                                  },
                                  'VAL_RN': {
                                    'type': 'float'
                                  },
                                  'VAL_SADT': {
                                    'type': 'float'
                                  },
                                  'VAL_SADTSR': {
                                    'type': 'float'
                                  },
                                  'VAL_SANGUE': {
                                    'type': 'float'
                                  },
                                  'VAL_SH': {
                                    'type': 'float'
                                  },
                                  'VAL_SH_FED': {
                                    'type': 'float'
                                  },
                                  'VAL_SH_GES': {
                                    'type': 'float'
                                  },
                                  'VAL_SP': {
                                    'type': 'float'
                                  },
                                  'VAL_SP_FED': {
                                    'type': 'float'
                                  },
                                  'VAL_SP_GES': {
                                    'type': 'float'
                                  },
                                  'VAL_TOT': {
                                    'type': 'float'
                                  },
                                  'VAL_TRANSP': {
                                    'type': 'float'
                                  },
                                  'VAL_UCI': {
                                    'type': 'float'
                                  },
                                  'VAL_UTI': {
                                    'type': 'float'
                                  },
                                  'VINCPREV': {
                                    'type': 'long'
                                  }
                        }
                }
            }

es.indices.create(index=indice,body=sih_type)