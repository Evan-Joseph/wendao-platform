<template>
  <div class="learning-path">
    <h2>您的学习路径</h2>
    <div id="learningPathGraph"></div>
  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
  data() {
    return {
      learningPathData: [
        {
          id: 1, name: '基础知识', children: [
            {id: 2, name: '概念 A'},
            {id: 3, name: '概念 B'}
          ]
        },
        {
          id: 4, name: '进阶知识', children: [
            {id: 5, name: '概念 C'},
            {id: 6, name: '概念 D'}
          ]
        }
      ]
    };
  },
  mounted() {
    this.drawLearningPath();
  },
  methods: {
    drawLearningPath() {
      const data = this.learningPathData;
      const width = 500, height = 400;

      const svg = d3.select('#learningPathGraph')
          .append('svg')
          .attr('width', width)
          .attr('height', height);

      const root = d3.hierarchy(data);
      const treeLayout = d3.tree().size([width - 20, height - 20]);

      treeLayout(root);

      // Links (连接节点的线)
      svg.selectAll('line')
          .data(root.links())
          .enter()
          .append('line')
          .attr('x1', d => d.source.x)
          .attr('y1', d => d.source.y)
          .attr('x2', d => d.target.x)
          .attr('y2', d => d.target.y)
          .attr('stroke', 'black');

      // Nodes (节点)
      svg.selectAll('circle')
          .data(root.descendants())
          .enter()
          .append('circle')
          .attr('cx', d => d.x)
          .attr('cy', d => d.y)
          .attr('r', 5)
          .attr('fill', 'blue');

      // Labels (标签)
      svg.selectAll('text')
          .data(root.descendants())
          .enter()
          .append('text')
          .attr('x', d => d.x + 10)
          .attr('y', d => d.y)
          .text(d => d.data.name)
          .attr('font-size', '12px')
          .attr('fill', 'black');
    }
  }
};
</script>

<style scoped>
.learning-path {
  max-width: 800px;
  margin: 0 auto;
  padding: 2em;
}
</style>
