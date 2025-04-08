document.addEventListener('DOMContentLoaded', () => {
    new fullpage('.fullpage', {
        // Configuración básica
        licenseKey: 'OPEN-SOURCE-GPLV3-LICENSE', // Clave gratuita
        scrollingSpeed: 800, // Velocidad del scroll
        navigation: true, // Menú de puntos
        navigationPosition: 'left', // Posición del menú

        // Eventos para transiciones
        onLeave: (origin, destination) => {
            // Oculta el contenido al salir de la sección
            const originContent = origin.item.querySelector('.fullpage__slide');
            originContent.style.opacity = '0';
            originContent.style.transform = 'translateY(-50px)';
        },
        afterLoad: (origin, destination) => {
            // Muestra el contenido al llegar a la sección
            const destinationContent = destination.item.querySelector('.fullpage__slide');
            destinationContent.style.opacity = '1';
            destinationContent.style.transform = 'translateY(0)';
        }
    });
});