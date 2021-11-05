const colors = require('tailwindcss/colors')

module.exports = {
    purge: [],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                beige: {
                    lightest: '#FFFFD4',
                    light: '#E6E6BE',
                    DEFAULT: '#BFBFA1',
                    dark: '#80806B',
                    darkest: '#404036',
                },
                emerald: colors.emerald,
                lime: colors.lime,
            },
            fontFamily: {
                sans: ['Lato', 'sans-serif'],
            },
        },
    },
    variants: {
        extend: {
            animation: ['hover', 'focus'],
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
