(function () {
    const input = document.querySelector('[id="faq-search-input"]');
    const results = Array.from(document.querySelectorAll('[data-faq-result]'));
    const emptyState = document.querySelector('[data-faq-empty]');

    if (!input || !emptyState) {
        return;
    }

    if (results.length === 0) {
        emptyState.hidden = false;
        return;
    }

    const normalize = function (value) {
        return value.toLowerCase().trim().replace(/\s+/g, ' ');
    };

    const filterResults = function () {
        const query = normalize(input.value);
        let visibleCount = 0;

        results.forEach(function (result) {
            const searchText = normalize(result.dataset.searchText || '');
            const isVisible = !query || searchText.includes(query);

            result.hidden = !isVisible;

            if (isVisible) {
                visibleCount += 1;
            }
        });

        emptyState.hidden = visibleCount !== 0;
    };

    input.addEventListener('input', filterResults);
}());
