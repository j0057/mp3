mp3.view.Analysis = Object.extend({
    constructor: function(selector, playlist) {
        this.$canvas = $(selector);
        this.context = this.$canvas[0].getContext("2d");

        this.playlist = playlist;

        this.last = 0;

        this.data = new Uint8Array(this.playlist.output.frequencyBinCount);

        this.animate = this.animate.bind(this);

        this.frequency = 60;

        window.requestAnimationFrame(this.animate);
    },
    animate: function(t) {
        if ((this.width != this.$canvas.width()) || (this.height != this.$canvas.height())) {
            this.width = this.$canvas.width();
            this.height = this.$canvas.height();
            this.$canvas
                .prop("width", this.width)
                .prop("height", this.height);
        }

        if ((t - this.last) >= (1000 / this.frequency)) {
            this.last = t;

            this.playlist.output.getByteFrequencyData(this.data);

            var image = this.context.getImageData(0, 0, this.width, this.height);
            this.context.clearRect(0, 0, this.width, this.height);       
            this.context.putImageData(image, -1, 0);

            for (var i = 0; i < this.playlist.output.frequencyBinCount; i++) {
                var v = 255 - this.data[i];
                this.context.fillStyle = "rgb(" + v + "," + v + "," + v + ")";
                this.context.fillRect(this.width - 1, this.playlist.output.frequencyBinCount- i, 1, 1); 
            };
        }

        window.requestAnimationFrame(this.animate);
    }
});
