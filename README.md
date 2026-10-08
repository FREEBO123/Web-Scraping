Proyecto de Web Scraping

Descripción del Proyecto:

el objetivo de este proyecto es lograr extraer informacion de la pagina del banco central de chile, con el fin de ejemplificar el metodo de extraccion de datos desde un sitio web, el proyecto actual se centrara netamente en el web scraping, todo lo que sea limpieza y analisis se trabajara en los proyectos siguientes

1. Web Scraping en Python desde la página del banco central:

    se uso la libreria Requests para las solicitudes HTML y BeautifulSoup para parsear el contenido
    y extraer la informacion relevante

2. Conversion a Dataframe

    el siguiente paso fue usar la libreria Pandas para convertir la informacion extraida en un Dataframe,
    de esa forma facilita la limpieza y transformacion.

3. Exportacion

    finalmente el dataframe resultante se exporta a formato excel, se debe mencionar que la informacion en si misma no esta limpia, se mantuvo los formatos y los errores que pueda haber en el arrastre, esto con el fin de ejemplificar su limpieza y transformaciones en el modulo siguiente "Limpieza y Graficos"