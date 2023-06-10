/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        'core/templates/core/*.html',
        'core/templates/core/includes/*.html',
        'veiculo/templates/veiculo/*.html',
        'veiculo/templates/veiculo/includes/*.html',
    ],
    theme: {
        extend: {},
    },
    corePlugins: {
        aspectRatio: false,
    },
    plugins: [
        require('@tailwindcss/typography'),
        require('@tailwindcss/forms'),
    ],
}