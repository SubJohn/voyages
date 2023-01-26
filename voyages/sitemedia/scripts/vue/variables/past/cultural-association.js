var_register_country = new TreeselectVariable({
    varName: "register_country",
    label: gettext("Register Country"),
    description: "",
  },{
    op: "is one of",
    searchTerm0: [],
  },{
    isImputed: false,
    isAdvanced: false
  });

var_ethnicity = new TreeselectVariable({
    varName: "ethnicity",
    label: gettext("Ethnicity"),
    description: "",
  },{
    op: "is one of",
    searchTerm: [],
  },{
    isImputed: false,
    isadvanced: false
  });


var_language_groups = new LanguageGroupVariable({
    varName: "language_groups",
    label: gettext("Language Groups"),
    description: gettext("Languages appear under a single modern country or under multi-country if they are geographically dispersed. Begin typing in the box below."),
  },{
    op: "is one of",
    searchTerm: [],
  },{
    isImputed: false,
    isadvanced: false,
    isUsed: true
  });

// all
culturalAssociation = {
  culturalAssociation: {
    var_register_country: var_register_country,
    var_ethnicity: var_ethnicity,
    var_language_groups: var_language_groups,

    count: {
      changed: 0,
      activated: 0,
    }
  },

  count: {
    changed: 0,
    activated: 0,
  },
}
