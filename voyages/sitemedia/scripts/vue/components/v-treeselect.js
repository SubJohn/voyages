// v-treeselect
Vue.component("v-treeselect", {
  props: ['title', 'description', 'varName', 'filter', "isImputed", "isAdvanced", "data"],
  template: `
  <div class="v-form-group">
    <div class="v-title">
      <span>{{title}}</span>
      <span>
        <b-badge
          v-if="isImputed"
          v-b-tooltip.hover title="Imputed variables are calculated by an algorithm and not based on historical records."
          variant="warning"
          class="v-badge-imputed">
          Imputed
        </b-badge>
        <b-badge
          v-if="isAdvanced"
          v-b-tooltip.hover title="Advanced variables are additional parameters that are frequenlty used. They do not change current search behavior."
          variant="danger" class="v-badge-advanced">Advanced</b-badge>
      </span>
    </div>
    <div class="v-description" v-text="description"></div>

    <div class="row">
      <div class="col-md-12">
        <treeselect
          :multiple="true"
          :load-root-options="loadRootOptions"
          placeholder="Select from the list"
          v-model="item.searchTerm0"
        />
      </div>
    </div>

    <div class="row v-padding">
      <div class="col-md-12">
        <code>{{item.searchTerm0}}</code>
      </div>
    </div>

    <div class="row v-padding">
      <div class="col-md-12">
        <b-button :disabled="!options.changed" variant="success" size="sm" @click="apply">Apply</b-button>
        <b-button :disabled="!options.changed" variant="secondary" size="sm" @click="reset">Reset</b-button>
      </div>
    </div>
  </div>

  `,

  components: {
    treeselect: window.VueTreeselect.Treeselect,
  },

  data: function(){
    return {
      item: {
        varName: this.varName,
        searchTerm0: this.filter.value.searchTerm0,
        searchTerm1: this.filter.value.searchTerm1,
        op: this.filter.value.op,
      },
      options: {
        searchTerm1Disabled: false,
        searchTermCaption0: null,
        searchTermCaption1: null,
        type: "text",
        changed: false,
      }
    }
  },

  methods: {
    // form action buttons
    apply() { // simply return the search string to whichever requested for it
      var searchString = JSON.stringify(this.item);
      alert(searchString);
    },
    reset() { // reset data; observers will take care of resetting the controls
      this.item.searchTerm0 = null;
      this.item.searchTerm1 = null;
    },
    loadRootOptions(callback) {
      callback(null, this.data)
    }
  },

  watch: {
    // search object
    item: {
      handler: function(){
        // control visibility
        if (this.item.searchTerm0 !== null && this.item.searchTerm0.length > 0) {
          this.options.changed = true;
          this.$emit('change', this.item, true);
        } else {
          this.options.changed = false;
          this.$emit('change', this.item, false);
        }
      },
      deep: true,
    },

    // update prop 'filter' from store
    filter: {
      handler: function(){
        if (!this.filter.changed) { // update when filter is not activated
          this.item.searchTerm0 = this.filter.value.searchTerm0;
          this.item.searchTerm1 = this.filter.value.searchTerm1;
          this.item.op = this.filter.value.op;
        }
      },
      deep: true,
    }
  },

  mounted: function() {
  },

});
// v-treeselect
