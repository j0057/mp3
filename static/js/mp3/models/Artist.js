mp3.models.Artist = mp3.base.CollectionResource.extend({
    itemType: Backbone.Collection.extend({ model: mp3.models.Album })
});
