class Translation(object):
    START_TEXT = """Hola,
Este es un bot de subida de URL de Telegram!

<b>Por favor envíeme cualquier enlace URL de descarga directa, puedo subirlo a telegram como archivo / video</b>

/help para más detalles.."""
    RENAME_403_ERR = "Lo siento. No se le permite cambiar el nombre de este archivo."
    ABS_TEXT = " Por favor no seas egoísta."
    UPGRADE_TEXT = "<b>👉 Crear su propio bot de clonación.. </b>  /help para detalles"
    FORMAT_SELECTION = "Seleccione el formato deseado: <a href='{}'>el tamaño del archivo puede ser aproximado</a> \nSi desea configurar una miniatura personalizada, envíe una foto antes o rápidamente después de tocar cualquiera de los botones a continuación.\nPuedes usar /deletethumbnail para eliminar la miniatura generada automáticamente."
    SET_CUSTOM_USERNAME_PASSWORD = """Si desea descargar videos premium, proporcione en el siguiente formato:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detectado. Utilice https://shrtz.me/PtsVnf6 y consígame una URL rápida para que pueda subir a Telegram, sin que me ralentice para otros usuarios.."
    DOWNLOAD_START = "tratando de descargar"
    UPLOAD_START = "tratando de subir"
    RCHD_BOT_API_LIMIT = "tamaño mayor que el tamaño máximo permitido (50 MB). Sin embargo, intentando subir."
    RCHD_TG_API_LIMIT = "Descargado en {} segundos.\nTamaño de archivo detectado: {}\nLo siento. Pero no puedo subir archivos de más de 1,5 GB debido a las limitaciones de la API de Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Por favor califíqueme si me encuentra útil. Únete: @"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Descargado en {} segundos. \nUnirse : @ \nSubido en {} segundos."
    NOT_AUTH_USER_TEXT = "Por favor /upgrade su suscripción."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Tamaño de archivo detectado: {}. Los usuarios gratuitos solo pueden cargar: {}\nActualice su suscripción.\nSi cree que esto es un error, comuníquese con <a href = 'https: //telegram.dog/'>@</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Miniatura de video / archivo personalizado guardada. Esta imagen se utilizará en el video / archivo.."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Miniatura personalizada borrada correctamente."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Los medios se borraron correctamente."
    SAVED_RECVD_DOC_FILE = "Documento descargado correctamente."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No se encontró ninguna ThumbNail personalizada."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> dicho: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> Añadido a {} hasta {}."
    CURENT_PLAN_DETAILS = """Detalles del plan actual
--------
ID de Telegram: <code> {} </code>
Nombre del plan: Usuario clonado gratuito
Expira el:"""
    HELP_USER = """Hai am URL Uploader bot..
    
1. Enviar URL (Enlace | Nuevo nombre con extensión).
2. Enviar miniatura personalizada (opcional).
3. Seleccione el botón.
    SVideo - Dar archivo como video con capturas de pantalla
    DFile - Dar archivo con capturas de pantalla
    Video: entregar archivo como video sin capturas de pantalla
    DFile: entregar archivo sin capturas de pantalla
   
<b>👉 Crea tu propio Clone Bot :</b> 👉 <a href="https://youtu.be/">Diploy</a>

--------
Envíeme a conocer los detalles del plan actual

Support Group : @
© @"""
    REPLY_TO_DOC_GET_LINK = "Responda a un medio de Telegram para obtener un enlace de descarga directa de alta velocidad"
    REPLY_TO_DOC_FOR_C2V = "Responder a un medio de Telegram para convertir"
    REPLY_TO_DOC_FOR_SCSS = "Responde a un medio de Telegram para obtener capturas de pantalla"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Responder a un medio de Telegram a /rename con soporte de miniaturas personalizadas"
    AFTER_GET_DL_LINK = "Enlace directo <a href='{}'>Generado</a> Válido por {} días.\n© @"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Sintaxis: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Primer envío /downloadmedia a cualquier medio para que pueda descargarse a mi local. \nEnviar /storageinfo para conocer los medios que se descargan actualmente."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Duración del video: {}\nEnviar /clearffmpegmedia para eliminar este medio, de mi almacenamiento.\nEnviar /trim HH:MM:SS [HH:MM:SS] para cu[l]t una pequeña foto / video, de los medios anteriores."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Ya existe un medio guardado. Por favor envíe /storageinfo para conocer los detalles actuales de los medios."
    USER_DELETED_FROM_DB = "Usuario <a href='tg://user?id={}'>{}</a> eliminado de la base de datos."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Responder a un medio de Telegram (MKV), para extraer transmisiones incrustadas"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Respuesta /generatecustomthumbnail a un álbum multimedia, para generar una miniatura personalizada"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "El álbum multimedia debe contener solo dos fotos. Vuelva a enviar el álbum multimedia y vuelva a intentarlo o envíe solo dos fotos en un álbum.."
    INVALID_UPLOAD_BOT_URL_FORMAT = "UEl formato RL es incorrecto. asegúrese de que su URL comience con http: // o https: //. Puede establecer un nombre de archivo personalizado mediante el enlace de formato | file_name.extension"
    ABUSIVE_USERS = "No se le permite utilizar este bot. Si cree que se trata de un error, marque /me para eliminar esta restricción."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/"
    EXTRACT_ZIP_INTRO_ONE = "Primero envíe un archivo comprimido, luego responda /unzip comando al archivo."
    EXTRACT_ZIP_INTRO_THREE = "Analizando archivo recibido. ⚠️ Esto puede llevar algún tiempo. Por favor sea paciente. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Lo siento. Se produjeron errores al procesar el archivo comprimido. Vuelve a comprobarlo todo dos veces y, si el problema persiste, infórmalo a <a href='https://telegram.dog/'>@</a>"
    EXTRACT_ZIP_STEP_TWO = """Seleccione file_name para cargar de las siguientes opciones.
Puedes usar /rename comando después de recibir el archivo para cambiarle el nombre con soporte de miniaturas personalizadas."""
    CANCEL_STR = "Proceso cancelado"
    ZIP_UPLOADED_STR = "Subió {} archivos en {} segundos"
    FREE_USER_LIMIT_Q_SZE = """No se puede procesar.
Usuarios gratuitos solo 1 solicitud cada 30 minutos.
/upgrade o intente 1800 segundos más tarde."""
    SLOW_URL_DECED = "Dios, eso parece ser una URL muy lenta. Como estabas jodiendo mi casa, no estoy de humor para descargar este archivo. Mientras tanto, ¿por qué no intentas esto: ==> https://shrtz.me/PtsVnf6 y me consigues una URL rápida para que pueda subir a Telegram, sin que me desacelere para otros usuarios?."
