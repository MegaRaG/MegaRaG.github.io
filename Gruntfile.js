module.exports = function(grunt) {
  
  // Configuration de Grunt
  grunt.initConfig({
    // Configuration des tâches Grunt ici
  });

  // Exemple de tâche pour minifier un fichier JS (vous pouvez ajouter d'autres plugins et tâches selon vos besoins)
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.initConfig({
    uglify: {
      my_target: {
        files: {
          'script/script.min.js': ['script/script.js']
        }
      }
    }
  });

  // Tâche par défaut
  grunt.registerTask('default', ['uglify']);
};
