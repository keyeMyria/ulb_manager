<template>
  <div>
    <!-- Standard -->
    <b-card header="Header"
            class="mb-2"
            title="Home page"
            sub-title="sample"
            show-footer>

      <icon name="refresh" spin></icon>
      Text

      <small slot="footer" class="text-muted">
        Home
      </small>

    </b-card>
  </div>

</template>

<script>
  export default {
    name: 'main'
  }
</script>
